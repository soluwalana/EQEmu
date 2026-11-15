/* Native WebGL2 zone geometry + Canvas2D tactical HUD. All positions remain EQ XYZ. */
(() => {
    'use strict';
    const cache = new Map(), views = new Map();
    const dot = (a, b) => a[0]*b[0] + a[1]*b[1] + a[2]*b[2];
    const sub = (a, b) => [a[0]-b[0], a[1]-b[1], a[2]-b[2]];
    const clamp = (x, lo, hi) => Math.max(lo, Math.min(hi, x));
    const valid = p => Array.isArray(p) && p.length >= 3 && p.slice(0,3).every(Number.isFinite);
    const MIN_ELEVATION = 0, MAX_ELEVATION = Math.PI / 2;
    const horizontalDistance = (a,b) => Math.hypot(a[0]-b[0],a[1]-b[1]);
    // Cover the viewport's full diagonal at top view, not just its short axis.
    const localRadius = (radius,zoom,w,h) => radius*zoom*Math.hypot(w,h)/Math.min(w,h);
    const shaders = {
        vertex: `#version 300 es
            in vec3 position;
            uniform vec3 center, right, up, nearAxis;
            uniform vec2 scale;
            uniform float depthScale, lift;
            out vec3 world; out vec3 bary;
            void main(){
                int i=gl_VertexID%3; bary=i==0?vec3(1,0,0):i==1?vec3(0,1,0):vec3(0,0,1);
                world=position; vec3 d=position-center; d.z+=lift;
                gl_Position=vec4(dot(d,right)*scale.x,dot(d,up)*scale.y,-dot(d,nearAxis)*depthScale,1.0);
            }`,
        fragment: `#version 300 es
            precision highp float;
            in vec3 world; in vec3 bary; uniform vec3 tint; uniform int navStyle;
            uniform float lowZ, highZ, opacity;
            uniform vec2 localCenter;
            uniform float localRange; out vec4 color;
            void main(){
                // Compute derivatives before fragment rejection at slice edges.
                vec3 n=normalize(cross(dFdx(world),dFdy(world)));
                // Cutaway is ONLY a world-Z plane, independent of the camera.
                if(world.z<lowZ || world.z>highZ) discard;
                // Optional local geometry is a player-centered circle, not a
                // camera-facing slab. Dither its outer band rather than writing
                // an opaque background-colored fragment over nearby geometry.
                if(localRange>0.0){
                    float d=length(world.xy-localCenter);
                    float keep=1.0-smoothstep(localRange*.85,localRange,d);
                    float threshold=fract(dot(floor(gl_FragCoord.xy),vec2(.75487766,.56984029)));
                    if(d>=localRange || threshold>=keep) discard;
                }
                float lighting=0.45+0.55*abs(dot(n,normalize(vec3(.35,.4,.85))));
                vec3 lit=tint*lighting;
                if(navStyle==1){ vec3 edge=smoothstep(vec3(0.0),fwidth(bary)*1.2,bary); lit=mix(lit*.55,lit,min(edge.x,min(edge.y,edge.z))); }
                color=vec4(lit,opacity);
            }`,
    };
    const sphereShaders = {
        vertex: `#version 300 es
            in vec3 unitPosition;
            in vec4 instanceCenterRadius;
            in vec3 instanceTint;
            uniform vec3 center, right, up, nearAxis;
            uniform vec2 scale; uniform float depthScale;
            out vec3 normal; out vec3 tint;
            void main(){
                vec3 d=instanceCenterRadius.xyz+unitPosition*instanceCenterRadius.w-center;
                normal=unitPosition; tint=instanceTint;
                gl_Position=vec4(dot(d,right)*scale.x,dot(d,up)*scale.y,-dot(d,nearAxis)*depthScale,1.0);
            }`,
        fragment: `#version 300 es
            precision highp float;
            in vec3 normal; in vec3 tint;
            uniform vec3 lightDirection, nearAxis;
            out vec4 color;
            void main(){
                vec3 n=normalize(normal);
                float diffuse=max(0.0,dot(n,lightDirection));
                float specular=pow(max(0.0,dot(n,normalize(lightDirection+nearAxis))),24.0);
                color=vec4(tint*(0.36+0.64*diffuse)+vec3(0.28*specular),1.0);
            }`,
    };
    function unitSphere() {
        const vertices=[], rings=10, slices=16;
        const point=(i,j)=>{
            const lat=Math.PI*i/rings, lon=2*Math.PI*j/slices;
            return [Math.sin(lat)*Math.cos(lon),Math.sin(lat)*Math.sin(lon),Math.cos(lat)];
        };
        for(let i=0;i<rings;i++)for(let j=0;j<slices;j++){
            const a=point(i,j),b=point(i+1,j),c=point(i+1,j+1),d=point(i,j+1);
            if(i!==rings-1)vertices.push(...a,...b,...c);
            if(i!==0)vertices.push(...a,...c,...d);
        }
        return new Float32Array(vertices);
    }
    function program(gl, sources=shaders) {
        const compile = (type, source) => {
            const s = gl.createShader(type); gl.shaderSource(s, source); gl.compileShader(s);
            if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) throw Error(gl.getShaderInfoLog(s));
            return s;
        };
        const p = gl.createProgram();
        const vs=compile(gl.VERTEX_SHADER,sources.vertex), fs=compile(gl.FRAGMENT_SHADER,sources.fragment);
        gl.attachShader(p,vs); gl.attachShader(p,fs); gl.linkProgram(p);
        gl.deleteShader(vs); gl.deleteShader(fs);
        if (!gl.getProgramParameter(p,gl.LINK_STATUS)) throw Error(gl.getProgramInfoLog(p));
        return p;
    }
    function fetchGeometry(zone) {
        if (cache.has(zone)) return cache.get(zone);
        const promise = fetch('/dashboard/geometry/'+encodeURIComponent(zone)+'?format=2').then(async response => {
            if (!response.ok) {
                let message=`HTTP ${response.status}`;
                try { message=(await response.json()).detail || message; } catch (_) {}
                throw Error(message);
            }
            const raw=await response.arrayBuffer(), h=new DataView(raw);
            if (raw.byteLength<20 || h.getUint32(0,true)!==0x32475145) throw Error('Invalid EQG2 geometry');
            const nc=h.getUint32(4,true), nn=h.getUint32(8,true), nw=h.getUint32(12,true), flags=h.getUint32(16,true);
            if (nc%3 || nn%3 || nw%3 || raw.byteLength!==20+12*(nc+nn+nw)) throw Error('Invalid geometry length');
            return {collision:new Float32Array(raw,20,nc*3), nav:new Float32Array(raw,20+nc*12,nn*3), water:new Float32Array(raw,20+(nc+nn)*12,nw*3), flags};
        });
        cache.set(zone,promise);
        // Retain two zones, not the entire map repository.
        while(cache.size>2) cache.delete(cache.keys().next().value);
        promise.catch(()=>{ if(cache.get(zone)===promise) cache.delete(zone); });
        return promise;
    }
    class View {
        constructor(id) {
            this.id=id; this.hud=document.getElementById(id); this.az=-.55; this.el=.72;
            this.follow=true; this.center=null; this.zoom=1; this.manualRadius=null; this.zone=null; this.generation=0;
            this.terrain=true; this.nav=true; this.water=true; this.cut=false; this.cutHeight=0; this.mode3d=true;
            this.localGeometry=false; this.showHiddenMobs=false;
            this.buffers=[]; this.geometry=null; this.minZ=null; this.error=''; this.latest=null; this.drag=null; this.skipClick=false;
            const glCanvas=document.createElement('canvas'); glCanvas.className='eq3d-gl';
            glCanvas.width=this.hud.width; glCanvas.height=this.hud.height;
            this.glCanvas=glCanvas;
            this.gl=glCanvas.getContext('webgl2',{antialias:true,alpha:false});
            if(!this.gl) throw Error('WebGL2 unavailable');
            const gl=this.gl; this.prog=program(gl); this.loc={};
            for(const name of ['center','right','up','nearAxis','scale','depthScale','lift','tint','lowZ','highZ','navStyle','opacity','localCenter','localRange'])
                this.loc[name]=gl.getUniformLocation(this.prog,name);
            this.attr=gl.getAttribLocation(this.prog,'position');
            gl.enable(gl.DEPTH_TEST); gl.clearColor(.039,.067,.105,1);
            this.initSpheres();
            const wrap=document.createElement('div'); wrap.className='eq3d-wrap';
            this.hud.before(wrap); wrap.append(glCanvas,this.hud); this.hud.classList.add('eq3d-hud');
            const tools=document.createElement('div'); tools.className='eq3d-tools'; wrap.before(tools);
            const info=document.createElement('p'); info.className='eq3d-info'; wrap.after(info); this.info=info;
            const button=(label,fn)=>{ const b=document.createElement('button');b.type='button';b.textContent=label;b.onclick=fn;tools.append(b);return b;};
            const check=(label,value,fn)=>{const l=document.createElement('label'), i=document.createElement('input');i.type='checkbox';i.checked=value;l.append(i,document.createTextNode(label));tools.append(l);i.onchange=()=>{fn(i.checked);this.redraw();};return i;};
            this.toggle=button('2D view',()=>{this.mode3d=!this.mode3d;this.toggle.textContent=this.mode3d?'2D view':'3D view';this.glCanvas.hidden=!this.mode3d;this.hud.classList.toggle('eq3d-hud',this.mode3d);this.redraw();});
            button('Follow player',()=>{this.resetCamera();this.redraw();});
            button('Top',()=>{this.el=MAX_ELEVATION;this.az=0;this.redraw();});
            button('Side',()=>{this.el=MIN_ELEVATION;this.az=0;this.redraw();});
            button('Orbit',()=>{this.el=.72;this.az=-.55;this.redraw();});
            button('Fit target',()=>this.fitTarget());
            check('Terrain',true,v=>this.terrain=v); check('Navmesh',true,v=>this.nav=v); check('Water',true,v=>this.water=v);
            check('Cutaway',false,v=>this.cut=v);
            check('Local geometry',false,v=>this.localGeometry=v);
            check('Show hidden mobs',false,v=>this.showHiddenMobs=v);
            const cut=document.createElement('input');cut.type='range';cut.min='0';cut.max='150';cut.value=String(this.cutHeight);cut.title='World-Z cut plane: player Z plus optional roof clearance';
            const label=document.createElement('label');label.append('Roof offset ',cut);tools.append(label);
            cut.oninput=()=>{this.cutHeight=Number(cut.value);this.redraw();};
            // Left drag pans; right/Alt drag orbits. Keep Shift/middle pan.
            // Only a real drag suppresses the subsequent marker click.
            this.hud.addEventListener('pointerdown',e=>{
                if(!this.mode3d || e.button>2 || this.drag)return;
                this.skipClick=false;
                this.drag={pointer:e.pointerId,x:e.clientX,y:e.clientY,startX:e.clientX,startY:e.clientY,
                    pan:e.shiftKey||e.button===1||(e.button===0&&!e.altKey),moved:false};
                this.hud.setPointerCapture(e.pointerId);
            });
            this.hud.addEventListener('pointermove',e=>{
                if(!this.drag||!this.mode3d||e.pointerId!==this.drag.pointer)return;
                const d=this.drag, camera=this.camera;
                if(!camera)return;
                if(!d.moved){
                    if(Math.hypot(e.clientX-d.startX,e.clientY-d.startY)<=4)return;
                    d.moved=true;
                    // Freeze the current base radius before manual navigation.
                    // Otherwise the overview's auto-fit can resize a panned map.
                    this.manualRadius=camera.radius;
                }
                const dx=e.clientX-d.x,dy=e.clientY-d.y;d.x=e.clientX;d.y=e.clientY;
                if(d.pan){
                    const r=this.hud.getBoundingClientRect();
                    const kx=camera.scale*r.width/this.hud.width,ky=camera.scale*r.height/this.hud.height;
                    if(kx<=0||ky<=0)return;
                    this.follow=false;
                    this.center=camera.center.map((v,i)=>v-dx*camera.right[i]/kx+dy*camera.up[i]/ky);
                }else{
                    this.az-=dx*.009;this.el=clamp(this.el+dy*.009,MIN_ELEVATION,MAX_ELEVATION);
                }
                this.redraw();
            });
            const end=e=>{
                if(this.drag?.pointer!==e.pointerId)return;
                if(this.drag.moved)this.skipClick=true;
                this.drag=null;
            };
            this.hud.addEventListener('pointerup',end);
            this.hud.addEventListener('pointercancel',end);
            this.hud.addEventListener('lostpointercapture',end);
            this.hud.addEventListener('contextmenu',e=>{if(this.mode3d)e.preventDefault();});
            this.hud.addEventListener('click',e=>{if(this.skipClick){this.skipClick=false;e.stopImmediatePropagation();}},true);
            this.hud.addEventListener('wheel',e=>{
                if(!this.mode3d)return;
                e.preventDefault();
                if(this.camera)this.manualRadius=this.camera.radius;
                this.zoom=clamp(this.zoom*Math.exp(e.deltaY*.001),.03,30);this.redraw();
            },{passive:false});
            this.glCanvas.addEventListener('webglcontextlost',e=>{e.preventDefault();this.error='WebGL context lost; use 2D view or reload';this.mode3d=false;this.glCanvas.hidden=true;this.hud.classList.remove('eq3d-hud');this.toggle.disabled=true;this.redraw();});
        }
        initSpheres(){
            const gl=this.gl, prog=program(gl,sphereShaders), loc={};
            for(const name of ['center','right','up','nearAxis','scale','depthScale','lightDirection'])
                loc[name]=gl.getUniformLocation(prog,name);
            const vertices=unitSphere(), vao=gl.createVertexArray(), mesh=gl.createBuffer(), instances=gl.createBuffer();
            gl.bindVertexArray(vao);
            gl.bindBuffer(gl.ARRAY_BUFFER,mesh);gl.bufferData(gl.ARRAY_BUFFER,vertices,gl.STATIC_DRAW);
            const position=gl.getAttribLocation(prog,'unitPosition');
            gl.enableVertexAttribArray(position);gl.vertexAttribPointer(position,3,gl.FLOAT,false,0,0);
            gl.bindBuffer(gl.ARRAY_BUFFER,instances);
            const placement=gl.getAttribLocation(prog,'instanceCenterRadius'), tint=gl.getAttribLocation(prog,'instanceTint');
            gl.enableVertexAttribArray(placement);gl.vertexAttribPointer(placement,4,gl.FLOAT,false,28,0);gl.vertexAttribDivisor(placement,1);
            gl.enableVertexAttribArray(tint);gl.vertexAttribPointer(tint,3,gl.FLOAT,false,28,16);gl.vertexAttribDivisor(tint,1);
            gl.bindVertexArray(null);
            this.spheres={prog,loc,vao,mesh,instances,count:vertices.length/3};
        }
        drawSpheres(instances,center,right,up,nearAxis,scale,depthScale,w,h){
            if(!instances.length)return;
            const gl=this.gl, sphere=this.spheres, l=sphere.loc;
            // Preserve diagnostic X-ray visibility through the map, but use
            // a fresh depth buffer so the spheres occlude each other in 3D.
            gl.clear(gl.DEPTH_BUFFER_BIT);
            gl.useProgram(sphere.prog);gl.bindVertexArray(sphere.vao);
            gl.uniform3fv(l.center,center);gl.uniform3fv(l.right,right);gl.uniform3fv(l.up,up);gl.uniform3fv(l.nearAxis,nearAxis);
            gl.uniform2f(l.scale,2*scale/w,2*scale/h);gl.uniform1f(l.depthScale,depthScale);
            const light=nearAxis.map((v,i)=>.8*v+.5*up[i]-.35*right[i]), length=Math.hypot(...light);
            gl.uniform3fv(l.lightDirection,light.map(v=>v/length));
            gl.bindBuffer(gl.ARRAY_BUFFER,sphere.instances);
            gl.bufferData(gl.ARRAY_BUFFER,new Float32Array(instances),gl.DYNAMIC_DRAW);
            gl.drawArraysInstanced(gl.TRIANGLES,0,sphere.count,instances.length/7);
            gl.bindVertexArray(null);
        }
        resetCamera(){this.follow=true;this.center=null;this.zoom=1;this.manualRadius=null;}
        resetZoom(){this.zoom=1;this.manualRadius=null;}
        redraw(){if(this.latest){const [radius,state,selected,hits,layout]=this.latest; if(this.mode3d)this.draw(radius,state,selected,hits,layout);else if(typeof window.EQMap3D.fallback==='function')window.EQMap3D.fallback(this.id,radius);}}
        fitTarget(){
            if(!this.latest)return;const [radius,s,selected]=this.latest;
            const target=[...s.mobs,...s.bots.filter(b=>b.spawned)].find(m=>m.id===selected);
            if(!target||!valid(target.position)){this.info.textContent='Select a mob or bot first.';return;}
            this.center=s.position.map((v,i)=>(v+target.position[i])/2);this.follow=false;
            this.manualRadius=radius;
            this.zoom=Math.max(12,Math.hypot(...sub(target.position,s.position))*.65)/radius;this.redraw();
        }
        load(zone){
            if(zone===this.zone)return;
            this.zone=zone;this.generation++;const generation=this.generation;
            this.resetCamera();this.geometry=null;this.minZ=null;this.error='';this.clearBuffers();
            if(!zone)return;
            fetchGeometry(zone).then(data=>{if(this.generation!==generation)return;this.geometry=data;this.upload(data);this.redraw();}).catch(e=>{if(this.generation!==generation)return;this.error=e.message;this.redraw();});
        }
        clearBuffers(){for(const b of this.buffers)this.gl.deleteBuffer(b.buffer);this.buffers=[];}
        upload(data){
            this.clearBuffers();const gl=this.gl;
            // Use collision and nav geometry, not water volumes, to constrain
            // manual camera panning to the actual map's lower bound.
            let minZ=Infinity;
            for(const vertices of [data.collision,data.nav])
                for(let i=2;i<vertices.length;i+=3)if(Number.isFinite(vertices[i]))minZ=Math.min(minZ,vertices[i]);
            this.minZ=Number.isFinite(minZ)?minZ:null;
            for(const [kind,vertices] of [['collision',data.collision],['nav',data.nav],['water',data.water]]){
                const buffer=gl.createBuffer();gl.bindBuffer(gl.ARRAY_BUFFER,buffer);gl.bufferData(gl.ARRAY_BUFFER,vertices,gl.STATIC_DRAW);
                this.buffers.push({kind,buffer,count:vertices.length/3});
            }
        }
        draw(radius,s,selected,hits,layout){
            this.latest=[radius,s,selected,hits,layout];this.load(s.zone);
            radius=this.manualRadius??radius;
            const hud=this.hud, gl=this.gl, w=hud.width,h=hud.height;
            if(this.minZ!==null&&!this.follow&&this.center)
                this.center[2]=Math.max(this.center[2],Math.min(this.minZ,s.position[2]));
            const center=this.follow||!this.center?s.position:this.center;
            this.el=clamp(this.el,MIN_ELEVATION,MAX_ELEVATION);
            const ca=Math.cos(this.az),sa=Math.sin(this.az),ce=Math.cos(this.el),se=Math.sin(this.el);
            const right=[ca,sa,0], up=[-sa*se,ca*se,ce], nearAxis=[sa*ce,-ca*ce,se];
            const scale=Math.min(w,h)/(2*radius*this.zoom), depthScale=1/Math.max(100000,radius*this.zoom*16);
            const project=p=>{const d=sub(p,center);return [w/2+dot(d,right)*scale,h/2-dot(d,up)*scale];};
            this.camera={center,right,up,scale,radius};
            gl.viewport(0,0,w,h);gl.clear(gl.COLOR_BUFFER_BIT|gl.DEPTH_BUFFER_BIT);gl.useProgram(this.prog);
            const l=this.loc;gl.uniform3fv(l.center,center);gl.uniform3fv(l.right,right);gl.uniform3fv(l.up,up);gl.uniform3fv(l.nearAxis,nearAxis);
            gl.uniform2f(l.scale,2*scale/w,2*scale/h);gl.uniform1f(l.depthScale,depthScale);
            const highZ=this.cut?s.position[2]+this.cutHeight:1e9;
            const range=localRadius(radius,this.zoom,w,h);
            gl.uniform1f(l.lowZ,-1e9);gl.uniform1f(l.highZ,highZ);
            // Full geometry is the default. The optional local footprint stays
            // fixed around the agent even while the camera pans or orbits.
            gl.uniform2f(l.localCenter,s.position[0],s.position[1]);
            gl.uniform1f(l.localRange,this.localGeometry?range:0);
            gl.bindVertexArray(null);gl.enableVertexAttribArray(this.attr);
            for(const b of this.buffers){
                if(!b.count||b.kind==='collision'&&!this.terrain||b.kind==='nav'&&!this.nav||b.kind==='water'&&!this.water)continue;
                gl.bindBuffer(gl.ARRAY_BUFFER,b.buffer);gl.vertexAttribPointer(this.attr,3,gl.FLOAT,false,0,0);
                const wet=b.kind==='water';
                gl.uniform1i(l.navStyle,b.kind==='nav'?1:0);gl.uniform1f(l.lift,b.kind==='nav'?.20:0);gl.uniform3fv(l.tint,wet?[.12,.55,.95]:b.kind==='nav'?[.20,.49,.39]:[.34,.43,.53]);
                gl.uniform1f(l.opacity,wet?.60:1);
                if(wet){gl.enable(gl.BLEND);gl.blendFunc(gl.SRC_ALPHA,gl.ONE_MINUS_SRC_ALPHA);gl.depthMask(false);}
                // Nav polygons sit slightly above collision surfaces. Depth
                // testing still reveals actual upper floors and occlusion.
                gl.drawArrays(gl.TRIANGLES,0,b.count);
                if(wet){gl.depthMask(true);gl.disable(gl.BLEND);}
            }
            const ctx=hud.getContext('2d');ctx.clearRect(0,0,w,h);ctx.font='12px monospace';
            const visible=p=>p[0]>=0&&p[0]<=w&&p[1]>=0&&p[1]<=h;
            // Match the geometry's world-space clipping rules. Full geometry
            // has no horizontal range limit; the screen projection handles
            // viewport culling independently of zoom and camera tilt.
            // A selected target remains an intentional X-ray diagnostic.
            const mobVisible=m=>this.showHiddenMobs || m.id===selected ||
                (m.position[2]<=highZ &&
                    (!this.localGeometry || horizontalDistance(m.position,s.position)<=range));
            const line=(a,b,color,dashed=false,width=1.5)=>{ctx.beginPath();ctx.moveTo(...a);ctx.lineTo(...b);ctx.strokeStyle=color;ctx.lineWidth=width;ctx.setLineDash(dashed?[5,4]:[]);ctx.stroke();ctx.setLineDash([]);};
            const circle=(p,r,color,stroke)=>{ctx.beginPath();ctx.arc(p[0],p[1],r,0,2*Math.PI);ctx.fillStyle=color;ctx.fill();if(stroke){ctx.strokeStyle=stroke;ctx.lineWidth=1.5;ctx.stroke();}};
            const label=(msg,p,color='#dce9f6')=>{const width=ctx.measureText(msg).width,x=clamp(p[0]+3,0,Math.max(0,w-width-6)),y=clamp(p[1]-15,0,h-17);ctx.fillStyle='#09111c';ctx.fillRect(x,y,width+6,17);ctx.fillStyle=color;ctx.fillText(msg,x+3,y+13);};
            const player=project(s.position), points=s.path?.points?.filter(valid)||[];
            if(points.length){const path=points;for(let i=1;i<path.length;i++)line(project(path[i-1]),project(path[i]),'#b7a4ff',true,2.5);if(valid(s.path.destination)){const p=project(s.path.destination);ctx.strokeStyle='#c9baff';ctx.strokeRect(p[0]-5,p[1]-5,10,10);}if(valid(s.path.next_point))circle(project(s.path.next_point),4,'#c9baff');}
            if(valid(s.movement?.asked))line(player,project(s.movement.asked),s.movement.refused?'#ec7784':'#5bc9d5',true,2);
            const entities=[], instances=[], botRadius=Math.max(8,6*Math.min(2,w/Math.max(1,hud.clientWidth)));
            const sphere=(point,pixels,tint)=>instances.push(...point,pixels/scale,...tint);
            const ring=(p,r,color)=>{ctx.beginPath();ctx.arc(p[0],p[1],r,0,2*Math.PI);ctx.strokeStyle=color;ctx.lineWidth=1.5;ctx.stroke();};
            let hiddenMobs=0;
            for(const m of s.mobs){
                if(m.dead||!valid(m.position))continue;
                const p=project(m.position);if(!visible(p))continue;
                if(!mobVisible(m)){hiddenMobs++;continue;}
                const size=m.aggro?7:5;
                sphere(m.position,size,entityTint(m).map(v=>v/255));
                if(m.id===selected)ring(p,size+2,'#fff');
                entities.push({x:p[0],y:p[1],id:m.id,name:m.name,radius:size,bot:false,los:m.los});
                if(m.id===selected||m.aggro)label(m.name,p);
            }
            const bots=layout(s.bots.filter(b=>valid(b.position)),project,w,h,botRadius,player);
            for(const b of bots){
                const dx=b.x-b.ax,dy=b.y-b.ay;
                if(Math.hypot(dx,dy)>1)line([b.ax,b.ay],[b.x,b.y],entityColor(b.bot,true));
                // Keep clustered bots independently clickable. Convert the
                // marker displacement back into the camera plane; its leader
                // line still identifies the true, unmodified bot position.
                const point=b.bot.position.map((v,i)=>v+(dx*right[i]-dy*up[i])/scale);
                sphere(point,botRadius,entityTint(b.bot,true).map(v=>v/255));
                if(b.bot.id===selected)ring([b.x,b.y],botRadius+2,'#fff');
                ctx.fillStyle='#103524';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText('B',b.x,b.y);ctx.textAlign='start';ctx.textBaseline='alphabetic';
                if(b.bot.id>0)entities.push({x:b.x,y:b.y,id:b.bot.id,name:b.bot.name,radius:botRadius,bot:true,los:b.bot.los});
            }
            if(visible(player)){
                const angle=s.heading*2*Math.PI/512, end=project([s.position[0]+Math.sin(angle)*14,s.position[1]+Math.cos(angle)*14,s.position[2]]);
                sphere(s.position,8,[.36,.79,.84]);ring(player,9,'#d0faff');
                const d=Math.hypot(end[0]-player[0],end[1]-player[1]);if(d>.01)line(player,[player[0]+(end[0]-player[0])/d*18,player[1]+(end[1]-player[1])/d*18],'#5bc9d5',false,3);
            }
            this.drawSpheres(instances,center,right,up,nearAxis,scale,depthScale,w,h);
            const target=[...s.mobs,...s.bots.filter(b=>b.spawned)].find(m=>m.id===selected);
            if(target&&valid(target.position)){
                const p=project(target.position), base=project([target.position[0],target.position[1],s.position[2]]), dz=target.position[2]-s.position[2];
                line(player,base,'#95b8cf',true);line(base,p,'#ecb36e',true,2);ring(p,9,'#ecb36e');label(`${target.name}  ΔZ ${dz>=0?'+':''}${dz.toFixed(1)} · ${losLabel(target)}`,p,'#ffe1b4');
            }
            ctx.fillStyle='#a4b8cb';ctx.fillText(`Z ${s.position[2].toFixed(1)} · ${Math.round(radius*this.zoom)} yd · ${Math.round(this.el*180/Math.PI)}° tilt`,10,h-12);
            if(s.path){const dz=valid(s.path.destination)?s.path.destination[2]-s.position[2]:null;ctx.fillText(`Path: ${s.path.mode??'—'}${s.path.fallback?' · FALLBACK':''}${dz!==null?' · destination ΔZ '+dz.toFixed(1):''}${s.movement?.refused?' · stride refused':''}`,10,h-29);}
            const axis=[w-35,h-32];for(const [v,color,name] of [[[1,0,0],'#ec7784','X'],[[0,1,0],'#6ccc91','Y'],[[0,0,1],'#699fe8','Z']]){const p=[axis[0]+dot(v,right)*22,axis[1]-dot(v,up)*22];line(axis,p,color,false,2);ctx.fillStyle=color;ctx.fillText(name,p[0],p[1]);}
            hits.set(this.id,entities);
            const count=s.bots.filter(b=>b.spawned).length;document.getElementById(this.id+'bots').textContent=`${bots.length} / ${count} spawned bots in view`;
            const data=this.geometry;this.info.textContent=this.error?`${this.error} · live entities still shown`:data?`${(data.collision.length/9).toLocaleString()} collision triangles · ${(data.nav.length/9).toLocaleString()} nav triangles · ${data.flags&4?(data.water.length/9).toLocaleString()+' water triangles':'No water map'} · ${this.cut?'Z ≤ '+(s.position[2]+this.cutHeight).toFixed(1):'All floors'} · ${this.localGeometry?'Local geometry '+Math.round(range)+' yd':'Full geometry'} · ${hiddenMobs} mobs hidden · route/spheres X-ray · drag pan, right/Alt-drag orbit, wheel zoom`:'Loading zone geometry…';
        }
    }
    window.EQMap3D={
        resetCamera(id){views.get(id)?.resetCamera();},
        resetZoom(id){views.get(id)?.resetZoom();},
        draw(id,radius,state,selected,hits,layout){
            if(!state||!valid(state.position))return false;
            let v=views.get(id);
            if(v===undefined){try{v=new View(id);views.set(id,v);}catch(e){views.set(id,null);console.warn('3D map unavailable',e);const note=document.createElement('p');note.className='eq3d-info';note.textContent='3D unavailable ('+e.message+'); showing 2D map.';document.getElementById(id).after(note);return false;}}
            if(!v)return false;v.latest=[radius,state,selected,hits,layout];
            if(!v.mode3d)return false;
            v.draw(radius,state,selected,hits,layout);return true;
        },
    };
})();

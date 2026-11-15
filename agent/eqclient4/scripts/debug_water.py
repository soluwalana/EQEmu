"""Render the upper boundary of the same liquid regions used by navigation."""
from __future__ import annotations

import math
from array import array

from eqclient4.nav.water import REGION_WATER, REGION_VWATER, _invert4, _transform_point

_WATER = {REGION_WATER, REGION_VWATER}


def _dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def _sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def _cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def _box(lo, hi):
    x, y, z = lo
    X, Y, Z = hi
    p = [(x,y,z),(X,y,z),(X,Y,z),(x,Y,z),(x,y,Z),(X,y,Z),(X,Y,Z),(x,Y,Z)]
    return [[p[i] for i in face] for face in ((0,3,2,1),(4,5,6,7),(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7))]


def _clip(faces, normal, split):
    """Clip a convex cell to dot(normal, p) + split <= 0, including its cap."""
    result, cap = [], []
    for face in faces:
        out = []
        a = face[-1]
        da = _dot(normal, a) + split
        for b in face:
            db = _dot(normal, b) + split
            if (da <= 0) != (db <= 0):
                t = da / (da - db)
                p = tuple(x + t*(y-x) for x,y in zip(a,b))
                out.append(p)
                if not any(math.dist(p, q) < 1e-6 for q in cap):
                    cap.append(p)
            if db <= 0:
                out.append(b)
            a, da = b, db
        if len(out) >= 3:
            result.append(out)
    if len(cap) >= 3:
        center = tuple(sum(p[i] for p in cap)/len(cap) for i in range(3))
        u = _cross(normal, (1,0,0) if abs(normal[0]) < .9*math.hypot(*normal) else (0,1,0))
        v = _cross(normal, u)
        un, vn = math.hypot(*u), math.hypot(*v)
        if un and vn:
            cap.sort(key=lambda p: math.atan2(_dot(_sub(p,center),v)/vn, _dot(_sub(p,center),u)/un))
            result.append(cap)
    return result


def _upper_faces(faces, out):
    # Determine outward orientation from the convex cell's interior. Only
    # upper faces are shown: no opaque volume walls hiding the terrain.
    points = [p for face in faces for p in face]
    if not points:
        return
    center = tuple(sum(p[i] for p in points)/len(points) for i in range(3))
    for face in faces:
        a = face[0]
        for i in range(1, len(face)-1):
            b,c = face[i:i+2]
            n = _cross(_sub(b,a), _sub(c,a))
            if _dot(n, _sub(a,center)) < 0:
                n = tuple(-x for x in n)
            if n[2] > 1e-8:
                for p in (a,b,c):
                    out.extend(p)


def water_vertices(water, bounds):
    """XYZ triangles for water/vwater top faces, including tilted OBBs.

    V1 BSP cells are clipped to the available zone geometry bounds. They are
    region boundaries, not client water textures or exact shoreline meshes.
    """
    out = array('f')
    if water is None:
        return out
    if water.version == 2:
        for region in water.regions:
            if region.kind not in _WATER:
                continue
            matrix = _invert4(region.inv)
            if matrix is None:
                continue
            faces = _box((region.min_x,region.min_y,region.min_z), (region.max_x,region.max_y,region.max_z))
            # WaterMap.region swaps EQ x/y before applying the inverse OBB.
            def eq(p):
                y,x,z = _transform_point(matrix,*p)
                return (x,y,z)
            _upper_faces([[eq(p) for p in face] for face in faces],out)
    elif water.version == 1 and water.nodes and bounds is not None:
        lo,hi = bounds
        todo = [(1, _box(lo,hi), frozenset())]
        while todo:
            index,faces,ancestors = todo.pop()
            if not faces or index in ancestors or not 1 <= index <= len(water.nodes):
                continue
            node = water.nodes[index-1]
            if not node.left and not node.right:
                if node.special in _WATER:
                    _upper_faces(faces,out)
                continue
            # BSP query also uses (y,x,z), so transform the plane normal.
            n = (node.normal[1],node.normal[0],node.normal[2])
            seen = ancestors | {index}
            if node.left:
                todo.append((node.left,_clip(faces,tuple(-x for x in n),-node.split),seen))
            if node.right:
                todo.append((node.right,_clip(faces,n,node.split),seen))
    return out

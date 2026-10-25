# Building EQEmu for AkkStack

Build inside the `eqemu-server` container, then point `server/bin` at those binaries. A macOS build of this tree will not run in AkkStack: the container is Debian 12 and `zone` is linked against the Perl built at `/opt/eqemu-perl`.

AkkStack mounts two directories into that container:

- `akk-stack/code` → `/home/eqemu/code` (source and `build/bin`)
- `akk-stack/server` → `/home/eqemu/server` (the running server)

`server/bin/world`, `zone`, and the other servers are symlinks to `code/build/bin`. That symlink step is the deploy.

Paths below assume:

- EQEmu checkout: `/Users/samo/work/EQEmu`
- AkkStack checkout: `/Users/samo/work/akk-stack`

## 1. Put this checkout where the container can see it

`make install` clones `https://github.com/EQEmu/EQEmu.git` into `akk-stack/code`, then `init-server-binaries` replaces whatever you built with the upstream release zip. For this tree, point `code` at it before you build:

```bash
cd /Users/samo/work/akk-stack
ln -sfn /Users/samo/work/EQEmu code
```

Docker Desktop follows that symlink. If it mounts an empty directory instead, set the volume in `docker-compose.yml` to `/Users/samo/work/EQEmu:/home/eqemu/code`.

Bring the stack up (`make up` from `akk-stack`, after `.env` exists). The image is `eqemulator/eqemu-server:v16`; it already has clang, CMake, ccache, Ninja, and the custom Perl.

## 2. Configure once inside the container

```bash
cd /Users/samo/work/akk-stack
make bash
make init-build
```

`init-build` initializes submodules (including vcpkg), deletes `~/code/build`, and configures with the flags AkkStack needs:

- `RelWithDebInfo`, Unix Makefiles, ccache
- login server and Lua on
- Perl from `/opt/eqemu-perl` (`libperl.so`, `perl`, and the `CORE` headers), not Debian’s Perl

The first configure compiles the vcpkg dependencies and takes a long time. Run `init-build` again only when those CMake flags need to change. `init-dev-build` is the same configure with Ninja, `-O0`, and tests turned on; after that, build with `ninja`, not `make build`.

## 3. Build and deploy

Still inside the container, the shell aliases in `assets/bash/.bash_aliases` are the intended loop. `source` means `cd ~/code/build`.

```bash
cd ~/code/build && make -j$(nproc)
~/assets/scripts/create-symlinks.pl
```

`create-symlinks.pl` force-symlinks these from `~/code/build/bin` onto `~/server/bin`:

- `eqlaunch`
- `export_client_files`
- `import_client_files`
- `loginserver`
- `queryserv`
- `shared_memory`
- `ucs`
- `world`
- `zone`

It also links patches and opcodes out of `~/code/utils/patches`.

The alias that does both the compile and the symlink is `update-source` (it also `git pull`s). Day-to-day rebuilds are `m`, which is `make -j$(nproc - 2)` in `~/code/build`. The container Makefile target `make build` is the same compile with one job.

Then bounce the processes so they load the new files:

```bash
cd ~/server && ./bin/spire spire:launcher restart
```

If the binary’s database schema changed, run `./bin/world database:updates` and `./bin/shared_memory` from `~/server` before that restart. Spire is already set to run shared memory on launch.

Leave the symlinks in place. `update-release` and `make init-server-binaries` download the release zip and replace them.

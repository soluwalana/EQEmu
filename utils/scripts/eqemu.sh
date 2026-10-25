#!/usr/bin/env bash
# Start, stop, and report the EQEmu processes for this server.
#
#   eqemu.sh start
#   eqemu.sh stop          # game processes; MariaDB keeps running
#   eqemu.sh stop all      # game processes and the mariadb container
#   eqemu.sh restart
#   eqemu.sh status
#
# The zone launcher defaults to "zone" (a small dynamic pool). Set
# EQEMU_LAUNCHER=peq to boot the static zone list instead.

RUN="${EQEMU_RUN:-$HOME/other/eqemu-run}"
DB_ENV="${EQEMU_DB_ENV:-$HOME/other/eqemu-data/mariadb.env}"
DB_CONTAINER="${EQEMU_DB_CONTAINER:-mariadb}"
LAUNCHER_NAME="${EQEMU_LAUNCHER:-zone}"

cd "$RUN"

pids_for() {
	local name="$1" pid cwd
	for pid in $(pgrep -x "$name" 2>/dev/null || true); do
		cwd="$(readlink -f "/proc/${pid}/cwd" 2>/dev/null || true)"
		if [[ "$cwd" == "$(readlink -f "$RUN")" ]]; then
			printf '%s\n' "$pid"
		fi
	done
}

running() {
	[[ -n "$(pids_for "$1")" ]]
}

wait_gone() {
	local name="$1" i
	for i in $(seq 1 30); do
		running "$name" || return 0
		sleep 1
	done
	return 1
}

stop_proc() {
	local name="$1" pid
	if ! running "$name"; then
		return 0
	fi
	echo "stopping ${name}"
	while read -r pid; do
		kill -TERM "$pid" 2>/dev/null || true
	done < <(pids_for "$name")
	if ! wait_gone "$name"; then
		echo "${name} did not exit; sending SIGKILL"
		while read -r pid; do
			kill -KILL "$pid" 2>/dev/null || true
		done < <(pids_for "$name")
	fi
}

start_daemon() {
	local name="$1"
	shift
	if running "$name"; then
		echo "${name} already running ($(pids_for "$name" | tr '\n' ' '))"
		return 0
	fi
	echo "starting ${name}"
	if [[ "$name" == "world" ]]; then
		FORCE_INTERACTIVE=1 nohup "$RUN/$name" "$@" >>"$RUN/logs/${name}.log" 2>&1 &
	else
		nohup "$RUN/$name" "$@" >>"$RUN/logs/${name}.log" 2>&1 &
	fi
}

db_running() {
	docker ps --filter "name=^/${DB_CONTAINER}$" --filter status=running --format '{{.Names}}' | grep -qx "$DB_CONTAINER"
}

wait_db() {
	# shellcheck disable=SC1090
	source "$DB_ENV"
	local i
	for i in $(seq 1 60); do
		if docker exec "$DB_CONTAINER" mariadb-admin ping -uroot -p"$MARIADB_ROOT_PASSWORD" --silent >/dev/null 2>&1; then
			return 0
		fi
		sleep 1
	done
	echo "MariaDB did not accept connections" >&2
	return 1
}

start_db() {
	if db_running; then
		echo "mariadb already running"
	else
		echo "starting mariadb"
		docker start "$DB_CONTAINER" >/dev/null
	fi
	wait_db
}

stop_db() {
	if db_running; then
		echo "stopping mariadb"
		docker stop "$DB_CONTAINER" >/dev/null
	fi
}

wait_world() {
	local i
	for i in $(seq 1 180); do
		if ! running world; then
			echo "world exited during startup. Last log lines:" >&2
			tail -n 30 "$RUN/logs/world.log" >&2
			return 1
		fi
		if ss -ltn | grep -q ':9000 '; then
			return 0
		fi
		sleep 1
	done
	echo "world did not listen on port 9000" >&2
	tail -n 30 "$RUN/logs/world.log" >&2
	return 1
}

cmd_start() {
	mkdir -p "$RUN/logs" "$RUN/shared" "$RUN/maps"
	start_db

	echo "building shared memory"
	if ! "$RUN/shared_memory" all >>"$RUN/logs/shared_memory.log" 2>&1; then
		echo "shared_memory failed. See $RUN/logs/shared_memory.log" >&2
		return 1
	fi

	start_daemon loginserver
	start_daemon world
	wait_world
	start_daemon ucs
	start_daemon queryserv
	start_daemon eqlaunch "$LAUNCHER_NAME"
	cmd_status
}

cmd_stop() {
	local with_db="${1:-}"
	# Stop the launcher before its zones, or it will start replacements.
	stop_proc eqlaunch
	stop_proc zone
	stop_proc world
	stop_proc ucs
	stop_proc queryserv
	stop_proc loginserver
	if [[ "$with_db" == "all" ]]; then
		stop_db
	fi
	cmd_status
}

cmd_status() {
	local name pid
	if db_running; then
		echo "mariadb  running"
	else
		echo "mariadb  stopped"
	fi
	for name in loginserver world ucs queryserv eqlaunch; do
		pid="$(pids_for "$name" | tr '\n' ' ')"
		if [[ -n "$pid" ]]; then
			echo "${name}  running  ${pid}"
		else
			echo "${name}  stopped"
		fi
	done
	pid="$(pids_for zone | wc -l | tr -d ' ')"
	echo "zone  ${pid} running"
}

usage() {
	echo "usage: $0 {start|stop|stop all|restart|status}" >&2
	exit 1
}

case "${1:-}" in
	start) cmd_start ;;
	stop) cmd_stop "${2:-}" ;;
	restart)
		cmd_stop
		cmd_start
		;;
	status) cmd_status ;;
	*) usage ;;
esac

#!/usr/bin/env bash

set -e

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

setup() {
    echo "Setting up..."

    if declare -F deactivate >/dev/null; then
        deactivate
    fi

    cd "$SCRIPT_DIR/agent"
    pyenv local 3.14.8

    if [[ "$(python --version)" != "Python 3.14.8" ]]; then
        echo "Python 3.14.8 is not installed or misconfigured" >&2
        return 1
    fi

    if [[ ! -d .venv ]]; then
        python -m venv .venv
    fi

    source .venv/bin/activate
    uv sync --all-extras
}

lint() {
    echo "Linting..."

    cd "$SCRIPT_DIR/agent"
    echo "Agent directory: $SCRIPT_DIR/agent"
    
    if [[ "$1" == "fix" ]]; then
        uv run ruff check --fix eqclient4
    fi
    
    uv run black eqclient4
    uv run isort --profile black eqclient4
    uv run mypy eqclient4

}

clean() {
    echo "Cleaning..."
    cd "$SCRIPT_DIR/agent"
    find . -type d -name '__pycache__' -prune -exec rm -rf {} +
    rm -rf .mypy_cache .pytest_cache

}

build() {
    echo "Building..."
}

run() {
    echo "Running..."
}

test() {
    echo "Testing..."
}

traces() {
    echo "Traces..."
}

usage() {
    echo "Usage: $0 {setup|lint|build|run|test|traces} [args...]"
    echo "  lint [agent|.epics|all]    Lint target (default: all)"
}

main() {
    local command="${1:-}"
    if [[ -z "$command" ]]; then
        usage
        return 1
    fi

    shift

    case "$command" in
        setup)  setup "$@" ;;
        lint)   lint "$@" ;;
        build)  build "$@" ;;
        run)    run "$@" ;;
        test)   test "$@" ;;
        clean)  clean "$@" ;;
        traces) traces "$@" ;;
        *)
            usage
            return 1
            ;;
    esac
}

main "$@"

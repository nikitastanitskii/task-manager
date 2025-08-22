
format:
	sh ./ci/tools/ci/autoflake.sh
	sh ./ci/tools/ci/isort.sh
	sh ./ci/tools/ci/black.sh

lint:
	sh ./ci/tools/ci/isort.sh --check-only
	sh ./ci/tools/ci/black.sh --check
	sh ./ci/tools/ci/flake8.sh

typecheck:
	sh ./ci/tools/ci/mypy.sh


all: lint typecheck
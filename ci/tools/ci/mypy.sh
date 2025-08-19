ADDITIONAL_ARGS=$*
mypy --config-file ci/tools/config/mypy.cfg $ADDITIONAL_ARGS -p src -p migrations

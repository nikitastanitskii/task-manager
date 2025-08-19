ADDITIONAL_ARGS=$*
isort --settings-path ci/tools/config/isort.cfg $ADDITIONAL_ARGS app/ tasks/ migrations/

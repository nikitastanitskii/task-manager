#!/bin/sh
autoflake --in-place --remove-all-unused-imports --ignore-init-module-imports --exclude models_init.py -r src/ migrations/

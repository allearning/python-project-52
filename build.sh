#!/usr/bin/env bash
# exit on error
# Render.com build script
set -o errexit

poetry install

python manage.py collectstatic --no-input
python manage.py migrate
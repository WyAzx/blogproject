#!/bin/sh
python /app/manage.py collectstatic --noinput
python /app/manage.py migrate

gunicorn blogproject.wsgi -b 0.0.0.0:9999 --chdir=/app
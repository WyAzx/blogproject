#!/bin/sh
python /app/manage.py collectstatic --noinput
python /app/manage.py migrate

gunicorn blogproject.wsgi -b 127.0.0.1:8011 --chdir=/app
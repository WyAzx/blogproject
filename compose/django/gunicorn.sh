#!/bin/sh
python /app/manage.py collectstatic --noinput
/usr/local/bin/gunicorn blogproject.wsgi -w 4 -b 127.0.0.1:8000 --chdir=/app
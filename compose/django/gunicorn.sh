#!/bin/sh
python /app/manage.py collectstatic --noinput
python /app/manage.py migrate

/usr/local/bin/gunicorn blogproject.wsgi -w 4 -b 127.0.0.1:8000 --chdir=/app/blogproject
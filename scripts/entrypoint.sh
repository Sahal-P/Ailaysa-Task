#!/bin/bash

cd ..
current_dir=$(pwd)
echo "Current working directory: $current_dir"

cd ./apps/api/core

python manage.py runserver

# gunicorn core.wsgi:application --bind 0.0.0.0:8000 --workers 3 --threads 3 --daemon
# pkill gunicorn
#  sudo service redis-server restart
celery -A core worker -l info -P gevent
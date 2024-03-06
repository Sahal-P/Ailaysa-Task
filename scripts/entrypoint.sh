#!/bin/bash

cd ..
current_dir=$(pwd)
echo "Current working directory: $current_dir"

cd ./apps/api/core

python manage.py runserver
#  sudo service redis-server restart
celery -A core worker -l info -P gevent
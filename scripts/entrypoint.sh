#!/bin/bash

cd ..
current_dir=$(pwd)
echo "Current working directory: $current_dir"

cd ./apps/api/core

python manage.py runserver

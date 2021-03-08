#!/usr/bin/env bash
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

python run.py
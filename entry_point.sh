#!/usr/bin/env bash
python3 manage.py db init
python3 manage.py db migrate
python3 manage.py db upgrade
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

python3 run.py
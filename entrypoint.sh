#! /bin/bash

python manage.py makemigrations --no-input

python manage.py migrate --no-input

python manage.py collectstatic --no-input

exec gunicorn very_interesting_project.wsgi:application -b 0.0.0.0:32777 --reload
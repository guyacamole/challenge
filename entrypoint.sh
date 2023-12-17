#!/bin/bash
. ./.env
python3 manage.py migrate
python3 manage.py makemigrations
python3 manage.py migrate

ls -l -a

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('${DJANGO_ADMIN_USERNAME}', '${DJANGO_ADMIN_EMAIL}', '${DJANGO_ADMIN_PASSWORD}')" | python manage.py shell
echo "django superuser created"
python3 manage.py runserver 0.0.0.0:${DJANGO_PORT}
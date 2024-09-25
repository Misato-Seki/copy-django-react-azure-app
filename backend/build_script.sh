python manage.py migrate

cd backend; echo "from django.contrib.auth.models import User; User.objects.create_superuser('${DJANGO_SUPERUSER_NAME}', '${DJANGO_SUPERUSER_EMAIL}', '${DJANGO_SUPERUSER_PASSWORD}')" | python manage.py shell
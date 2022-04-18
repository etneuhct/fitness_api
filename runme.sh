python manage.py migrate
daphne django_server.asgi:application -p 8000 & nginx -g "daemon off;"
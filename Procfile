release: python3 manage.py makemigrations --no-input
release: python3 manage.py migrate --no-input
web: gunicorn ValidationAPI.wsgi
web: gunicorn ValidationAPI:locks --timeout 10
web: gunicorn ValidationAPI:face_api --max-requests 1200
release: python3 manage.py makemigrations --no-input
release: python3 manage.py migrate --no-input
web: gunicorn ValidationAPI.wsgi
# worker: python face_api/worker.py
web: gunicorn --bind 127.0.0.1:8000 --workers=3 --threads=20 olx_demo.wsgi:application
celery_worker: celery -A olx_demo beat -l INFO
celery_beat: celery -A olx_demo worker --pool=solo -l info

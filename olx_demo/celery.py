from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'olx_demo.settings')
app = Celery('olx_demo')
app.conf.enable_utc = False
CELERY_TIMEZONE = 'UTC'
# app.conf.update(timezone='Asia/Kolkata')
app.config_from_object(settings, namespace='CELERY')
app.conf.beat_schedule = {
    'get_result': {
        'task': 'products.tasks.project_results',
        'schedule': 86400.0,
    }
}
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
from __future__ import absolute_import , unicode_literals

import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mbm_minor.settings')

app = Celery('mbm_minor')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()



# app.conf.beat_schedule = {
#     'send-every-day-morning': {
#         'task': 'predictor.tasks.adding',
#         'schedule': 30.0,
#     }
#    }
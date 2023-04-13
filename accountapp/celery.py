from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'accountapp.settings')
app = Celery('accountapp')



app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'send-data-every-10-minutes':{
        'task': 'account.tasks.instagram_data',
        'schedule': crontab('*/10'),
        
    }
}



@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

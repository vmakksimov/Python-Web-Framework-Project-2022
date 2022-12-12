import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Crypto_web.settings')
app = Celery('Crypto_web')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

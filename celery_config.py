from celery import Celery
from dotenv import load_dotenv
import os

load_dotenv()

celery = Celery('tasks', broker=os.getenv('CELERY_BROKER_URL'))

celery.conf.update(
    result_backend=os.getenv('CELERY_RESULT_BACKEND'),
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)
from celery import Celery
from celery.schedules import crontab
import asyncio

celery = Celery('worker', broker='redis://localhost:6379')
celery_event_loop = asyncio.new_event_loop()

celery.autodiscover_tasks()
celery.conf.beat_schedule = {
    "add-every-300-seconds": {
        "task": "worker.tasks.test_task",
        'schedule': crontab(minute='*/5'),
    },
}

celery.conf.timezone = 'UTC'

if __name__ == '__main__':
    celery.start()
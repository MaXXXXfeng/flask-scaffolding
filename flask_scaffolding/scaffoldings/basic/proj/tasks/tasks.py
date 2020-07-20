import requests

from proj.extensions import celery


@celery.task
def print_periodic_info():
    print('This is a sample periodic task')

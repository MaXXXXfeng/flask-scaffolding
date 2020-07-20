import logging
import os
import datetime


class Config(object):
    # noinspection PyPackageRequirements
    DEBUG = False

    LOG_FORMAT = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
    LOG_LEVEL = logging.INFO

    #  发件箱设置
    SMTP = {
        'host': 'smtp.exmail.qq.com',
        'port': 0,
        'username': 'itservice@xxx.com.cn',
        'password': '',
        'use_ssl': False,
        'use_tls': False,
        'fromname': 'APP Name <itservice@xxx.com.cn>'
    }
    DEV_EMAIL = 'xxxx@xx.com.cn'

    # celery设置
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379/1')
    CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379/2')

    # celery定时任务设置
    CELERYBEAT_UPDATE_FREQUENCY = 600
    CELERY_ACCEPT_CONTENT = ['json', 'pickle']
    CELERY_TASK_SERIALIZER = 'pickle'
    CELERY_RESULT_SERIALIZER = 'pickle'
    CELERYBEAT_SCHEDULE = {
        'update-annotators-every-10-minutes': {
            'task': 'proj.tasks.tasks.update_annotators_statistics',
            'schedule': datetime.timedelta(seconds=CELERYBEAT_UPDATE_FREQUENCY),
            'args': ()
        },
    }
    CELERY_TIMEZONE = 'UTC'

    # Flask-SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@host/db?charset=utf8'
    SQLALCHEMY_POOL_RECYCLE = 3600
    SQLALCHEMY_POOL_SIZE = 5
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-MongoEngine settings
    MONGO_DATABASE = 'db name'
    MONGO_SERVER = 'server url'
    MONGO_PORT = 28017
    MONGO_USER = 'user'
    MONGO_PASSWORD = 'password'
    MONGODB_SETTINGS = {
        'db': 'db name',
        'host': f'mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_SERVER}:{MONGO_PORT}/{MONGO_DATABASE}?authSource=admin'
    }

    # ETCD配置
    ETCD_HOST = os.environ.get('ETCD_URL', '127.0.0.1')
    ETCD_PORT = int(os.environ.get('ETCD_PORT', 2379))


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    LOG_LEVEL = logging.WARNING


def get_config_class():
    env = os.environ.get('proj_env'.upper(), 'dev').lower()
    if env == 'prod':
        return ProductionConfig
    return DevelopmentConfig


CONF = get_config_class()

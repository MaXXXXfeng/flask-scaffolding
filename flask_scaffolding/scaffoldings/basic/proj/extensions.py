from flask_mongoengine import MongoEngine
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from celery import Celery
import etcd3

from proj.config import CONF

mongo_db = MongoEngine()
sql_db = SQLAlchemy()
migrate = Migrate()
celery = Celery(__name__, broker=CONF.CELERY_BROKER_URL)
etcd = etcd3.client(host=CONF.ETCD_HOST, port=CONF.ETCD_PORT)
from sqlalchemy import Column, Integer, SmallInteger, String, Text, DateTime, Boolean
from sqlalchemy import TypeDecorator, ForeignKey, inspect

from proj.config import CONF
from proj.extensions import sql_db


class ModelMixin(object):
    def save(self):
        sql_db.session.add(self)
        sql_db.session.commit()


class TimestampMixin(object):
    created_at = Column(DateTime, default=now, nullable=False)
    updated_at = Column(DateTime, default=now, onupdate=now, nullable=False)


class MySqlModel(sql_db.Model, ModelMixin, TimestampMixin):
    __tablename__ = 'my_model'

    id = Column(Integer, primary_key=True)

    def to_dict(self):
        return {
            'id': self.id
        }

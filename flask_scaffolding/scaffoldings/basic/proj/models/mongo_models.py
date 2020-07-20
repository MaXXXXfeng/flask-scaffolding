from mongoengine import (
    DateTimeField,
    StringField,
    DictField,
    ObjectIdField,
    ListField,
    IntField,
    BooleanField,
)

from proj.extensions import mongo_db
from proj.utils import utcnow


class TimestampMixin(object):
    created_at = DateTimeField(required=True, default=utcnow())
    updated_at = DateTimeField(required=True)


class ModelMixin(mongo_db.Document):
    meta = {'abstract': True}

    def save(self):
        self.updated_at = utcnow()
        super().save()


class MyMongoModel(ModelMixin, TimestampMixin):
    _id = IntField(primary_key=True)

    def to_dict(self):
        return {
            'id': self.id
        }


class Sequence(mongo_db.Document):
    ''' Generate Auto incrementing IDs by using next_sequence_id method '''
    _id = StringField(primary_key=True)
    value = IntField(required=True)

    @classmethod
    def next_sequence_id(cls, name):
        collection = cls._get_collection()
        document = collection.find_one_and_update(
            {"_id": name}, {"$inc": {"value": 1}},
            return_document=True)
        return document["value"]

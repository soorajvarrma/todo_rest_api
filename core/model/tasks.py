"""ORM document format

Keyword arguments:
argument -- description
Return: return_description
"""

import datetime
from mongoengine import Document, DateField, StringField, BooleanField
from marshmallow import Schema, fields, pre_dump


class Task(Document):
    """Documents the format"""

    task = StringField(required=True)
    done = BooleanField()
    date = DateField()


class TaskSchema(Schema):
    """Schema for serialization"""

    id = fields.Str(dump_only=True)
    task = fields.String(required=True)
    done = fields.Boolean()
    date = fields.Date()


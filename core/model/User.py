from mongoengine import Document, StringField, EmailField
from marshmallow import Schema, fields

class User(Document):
    """Documents the format
    """
    username = StringField(required=True, unique=True, max_length=150)
    email = EmailField(required=True, unique=True, max_length=150)
    password = StringField(required=True)

    
class UserSchema(Schema):
    """Schema for serialization"""
    id = fields.Str(dump_only=True)
    username = fields.String(required=True)
    email = fields.String(required=True)
    password = fields.String(required=True, load_only=True)
    
    
class UserLoginSchema(Schema):
    """Schema for serialization"""
    id = fields.Str(dump_only=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
from mongoengine import *


class Name_Info(EmbeddedDocument):
    short_en = StringField(required=True, max_length=50)
    short_zh = StringField(required=True, max_length=100)
    name_en = StringField(required=True, max_length=50)
    name_zh = StringField(required=True, max_length=100)


class Area(EmbeddedDocument):
    Name = StringField()
    Capacity = StringField()
    Opened = StringField()
    TicketPrice = StringField()
    Address = StringField()

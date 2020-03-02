import os
from utils import config
from mongoengine import *
from mongoengine.queryset.visitor import Q
from datetime import datetime


# os.chdir("..")
rootpath = os.getcwd()
config = config.configuration(rootpath)
try:
    connect(db=config.getconfig("DatawareHouse", "DBname"), username=config.getconfig("DatawareHouse", "Account"), password=config.getconfig("DatawareHouse", "Password"), host=config.getconfig("DatawareHouse", "FullURL"))
except ConnectionError:
    print("Could not connect to MongoDB", file=stderr)

class sport_type(Document):
    sport_type_id = IntField()
    name_en = StringField(required=True, max_length=50)
    name_zh = StringField(required=True, max_length=100)
    memo = StringField(max_length=50)
    update_user = StringField(max_length=50)
    update_time = DateTimeField(required = False)
    create_time = DateTimeField()

    def find(Q):
        return sport_type.objects(Q)

    def findcount(Q):
        return sport_type.objects(Q).count()

    def findfirst(Q):
        return sport_type.objects(Q).first()

basketball = sport_type()
basketball.sport_type_id =1
basketball.name_en = "basketball"
basketball.name_zh = "籃球"
basketball.memo = ""
basketball.update_time = datetime.now()
basketball.create_time = datetime.now()
basketball.save()

football = sport_type()
football.sport_type_id =2
football.name_en = "football"
football.name_zh = "足球"
football.memo = ""
football.update_time = datetime.now()
football.create_time = datetime.now()
football.save()
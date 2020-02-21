import os
from utils import config
from mongoengine import *
from mongoengine.queryset.visitor import Q
from datetime import datetime
from model.dto import Name_Info as Name_InfoObject
from model.dto import Area as AreaObject
from model.dto import Coach as CoachObject

os.chdir("..")
rootpath = os.getcwd()
config = config.configuration(rootpath)
try:
    connect(db=config.getconfig("DatawareHouse", "DBname"), username=config.getconfig("DatawareHouse", "Account"), password=config.getconfig("DatawareHouse", "Password"), host=config.getconfig("DatawareHouse", "FullURL"))
except ConnectionError:
    print("Could not connect to MongoDB", file=stderr)

class team_basic_data(Document):
    league_category = IntField()
    sport_type = IntField()
    name_info = EmbeddedDocumentField(Name_InfoObject)
    league_area = IntField()
    logo = StringField(required=True, max_length=50)
    nationalid = IntField()
    national_flag = StringField(required=True, max_length=50)
    national_name_en = StringField(required=True, max_length=50)
    national_name_zh = StringField(required=True, max_length=50)
    city_en = StringField(required=True, max_length=50)
    city_zh = StringField(required=True, max_length=50)
    estableish_date = DateTimeField(required = False)
    join_date = DateTimeField(required=True)
    area_info = EmbeddedDocumentField(AreaObject)
    coach_info = EmbeddedDocumentField(CoachObject)
    memo = StringField(max_length=50)
    update_user = StringField(max_length=50)
    update_time = DateTimeField(required=False)
    create_time = DateTimeField()

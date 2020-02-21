import os
from utils import config
from mongoengine import *
from mongoengine.queryset.visitor import Q
from datetime import datetime
from model.dto import Name_Info as Name_InfoObject
from model.dto import Basketball_match_record as Basketball_match_recordObject
from model.dto import Football_match_record as Football_match_recordObject

os.chdir("..")
rootpath = os.getcwd()
config = config.configuration(rootpath)
try:
    connect(db=config.getconfig("DatawareHouse", "DBname"), username=config.getconfig("DatawareHouse", "Account"), password=config.getconfig("DatawareHouse", "Password"), host=config.getconfig("DatawareHouse", "FullURL"))
except ConnectionError:
    print("Could not connect to MongoDB", file=stderr)

class player_match_record_history(Document):
    matchid = ObjectIdField()
    playerid = ObjectIdField()
    leagueid = ObjectIdField()
    seasonid = IntField()
    sport_type = IntField()
    name_info = EmbeddedDocumentField(Name_InfoObject)
    record = DictField()
    update_user = StringField(max_length=50)
    update_time = DateTimeField(required=False)
    create_time = DateTimeField()
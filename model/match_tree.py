import os
from utils import config
from mongoengine import *
from mongoengine.queryset.visitor import Q
from datetime import datetime
from model.dto import Match_Team_Info as Match_Team_InfoObject
from model.dto import Match_Playerd_Recrod as Match_Playerd_RecrodObject
from model.dto import Area as AreaObject
from model.dto import Football_match_record as Football_match_recordObject
from model.dto import Basketball_match_record as Basketball_match_recordObject


os.chdir("..")
rootpath = os.getcwd()
config = config.configuration(rootpath)
try:
    connect(db=config.getconfig("DatawareHouse", "DBname"), username=config.getconfig("DatawareHouse", "Account"), password=config.getconfig("DatawareHouse", "Password"), host=config.getconfig("DatawareHouse", "FullURL"))
except ConnectionError:
    print("Could not connect to MongoDB", file=stderr)

class match_info(EmbeddedDocument):
    matchid = ObjectIdField()
    groupname = FileField()
    left_match = EmbeddedDocumentListField()
    right_match = EmbeddedDocumentListField()
    home_info = EmbeddedDocumentListField()
    away_info = EmbeddedDocumentListField()
    home_socre = IntField()
    away_score = IntField()


class match_tree(Document):
    leagueid = IntField()
    model_type = IntField()#type 1淘汰賽 2.雙淘汰賽 3.小組賽
    match_info = EmbeddedDocumentListField(match_info)
    update_user = StringField(max_length=50)
    update_time = DateTimeField(required=False)
    create_time = DateTimeField()
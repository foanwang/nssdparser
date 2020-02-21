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

class match_detail(Document):
    matchid = StringField()
    match_time = DateTimeField()
    sport_type = IntField()
    race_no = IntField()
    season_type = IntField()
    home_team_info = EmbeddedDocumentField(Match_Team_InfoObject)
    away_team_info = EmbeddedDocumentField(Match_Team_InfoObject)
    home_players = EmbeddedDocumentListField(Match_Playerd_RecrodObject)
    away_players = EmbeddedDocumentListField(Match_Playerd_RecrodObject)
    home_score = IntField()
    away_score = IntField()
    home_data = DictField()
    away_data = DictField()
    arena_data = EmbeddedDocumentField(AreaObject)
    stageinfo = EmbeddedDocumentField() #
    status = IntField()
    update_user = StringField(max_length=50)
    update_time = DateTimeField(required=False)
    create_time = DateTimeField()

    def find(Q):
        return position.objects(Q)

    def findcount(Q):
        return position.objects(Q).count()


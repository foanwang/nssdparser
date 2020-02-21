import os
from utils import config
from mongoengine import *
from mongoengine.queryset.visitor import Q
from datetime import datetime
from model.dto import Area as Area_InfoObject
from model.dto import Match_team_info as Match_Team_InfoObject


os.chdir("..")
rootpath = os.getcwd()
config = config.configuration(rootpath)
try:
    connect(db=config.getconfig("DatawareHouse", "DBname"), username=config.getconfig("DatawareHouse", "Account"), password=config.getconfig("DatawareHouse", "Password"), host=config.getconfig("DatawareHouse", "FullURL"))
except ConnectionError:
    print("Could not connect to MongoDB", file=stderr)

class match(Document):
    league_category_id = IntField()
    year = IntField()
    race_no = IntField()
    sport_type = IntField()
    season_type = IntField()
    home_info = EmbeddedDocumentField(Match_Team_InfoObject)
    away_info = EmbeddedDocumentField(Match_Team_InfoObject)
    arena_data = EmbeddedDocumentField(Area_InfoObject)
    status = IntField()# 0 未賽 1正在比賽 2已賽
    update_user = StringField(max_length=50)
    update_time = DateTimeField(required=False)
    create_time = DateTimeField()


    def find(Q):
        return player_basic_data.objects(Q)

    def findcount(Q):
        return player_basic_data.objects(Q).count()
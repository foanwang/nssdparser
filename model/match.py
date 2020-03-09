import os
from utils import config
from mongoengine import *
from mongoengine.queryset.visitor import Q
from datetime import datetime
from model.dto import Arena
from model.dto import Match_Team_Info


# os.chdir("..")
rootpath = os.getcwd()
config = config.configuration(rootpath)
try:
    connect(db=config.getconfig("DatawareHouse", "DBname"), username=config.getconfig("DatawareHouse", "Account"), password=config.getconfig("DatawareHouse", "Password"), host=config.getconfig("DatawareHouse", "FullURL"))
except ConnectionError:
    print("Could not connect to MongoDB", file=stderr)

class match(Document):
    leagueid = ObjectIdField()
    year = StringField()
    race_no = IntField()
    sport_type = IntField()
    season_type = IntField()
    home_info = EmbeddedDocumentField(Match_Team_Info)
    away_info = EmbeddedDocumentField(Match_Team_Info)
    arena_data = EmbeddedDocumentField(Arena)
    status = IntField()# 0 未賽 1正在比賽 2已賽
    match_time = IntField()
    referenceId = IntField()#第三方的data id
    update_user = StringField(max_length=50, required=False)
    update_time = DateTimeField(required=False)
    create_time = DateTimeField()

    def find(Q):
        return match.objects(Q)

    def findcount(Q):
        return match.objects(Q).count()

    def findfirst(Q):
        return match.objects(Q).first()

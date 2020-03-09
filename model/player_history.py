import os
from utils import config
from mongoengine import *
from mongoengine.queryset.visitor import Q
from datetime import datetime
from model.dto import Name_Info as Name_InfoObject


# os.chdir("..")
rootpath = os.getcwd()
config = config.configuration(rootpath)
try:
    connect(db=config.getconfig("DatawareHouse", "DBname"), username=config.getconfig("DatawareHouse", "Account"), password=config.getconfig("DatawareHouse", "Password"), host=config.getconfig("DatawareHouse", "FullURL"))
except ConnectionError:
    print("Could not connect to MongoDB", file=stderr)

class player_history(Document):
    leagueid = ObjectIdField()
    teamid = ObjectIdField()
    playerid = ObjectIdField()
    year = StringField()
    season_type = IntField()
    sport_type = IntField()
    detail = DictField()
    rank = IntField()
    update_user = StringField(max_length=50)
    update_time = DateTimeField(required=False)
    create_time = DateTimeField()

    def find(Q):
        return player_history.objects(Q)

    def findcount(Q):
        return player_history.objects(Q).count()


    def findTeamHistoryByTeamId(ObjectId):
        return player_history.objects(Q(teamid=ObjectId))

    def findPlayerHistoryByLeagueidandTeamidandPlayeridandYear(leagueid, teamid, playerid,  year):
        return player_history.objects(Q(leagueid=leagueid, teamid=teamid, playerid=playerid, year=year)).first()
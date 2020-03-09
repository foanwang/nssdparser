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



class team_history(Document):
    leagueid = ObjectIdField()
    teamid = ObjectIdField()
    year = StringField()
    season_type = IntField()
    sport_type = IntField()
    detail = DictField()
    update_user = StringField(max_length=50)
    update_time = DateTimeField(required=False)
    create_time = DateTimeField()

    def find(Q):
        return team_history.objects(Q)

    def findcount(Q):
        return team_history.objects(Q).count()

    def findfirst(Q):
        return team_history.objects(Q).first()

    def findTeamHistoryByTeamId(ObjectId):
        return team_history.objects(Q(teamid=ObjectId))

    def findTeamHistoryByLeagueandTeamidandYear(leagueid , teamid, year):
        return team_history.objects(Q(leagueid=leagueid, teamid=teamid, year=year)).first()


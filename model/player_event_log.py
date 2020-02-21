import os
from utils import config
from mongoengine import *
from mongoengine.queryset.visitor import Q
from datetime import datetime
from model.dto import Name_Info as Name_InfoObject
from model.dto import TeamInfo as Team_InfoObject
from model.dto import NationaL_Info as National_InfoObject


os.chdir("..")
rootpath = os.getcwd()
config = config.configuration(rootpath)
try:
    connect(db=config.getconfig("DatawareHouse", "DBname"), username=config.getconfig("DatawareHouse", "Account"), password=config.getconfig("DatawareHouse", "Password"), host=config.getconfig("DatawareHouse", "FullURL"))
except ConnectionError:
    print("Could not connect to MongoDB", file=stderr)

class player_event_log(Document):
    teamid = StringField()
    action = StringField()
    actiontime = DateTimeField(required=False)
    update_user = StringField(max_length=50)
    update_time = DateTimeField(required=False)
    create_time = DateTimeField()

    def find(Q):
        return player_basic_data.objects(Q)

    def findcount(Q):
        return player_basic_data.objects(Q).count()

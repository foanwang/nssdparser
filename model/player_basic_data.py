import os
from utils import config
from mongoengine import *
from mongoengine.queryset.visitor import Q
from datetime import datetime
from model.dto import Name_Info as Name_InfoObject
from model.dto import Team_Info as Team_InfoObject
from model.dto import National_Info as National_InfoObject
from model.dto import Basketball_Property_Info as Basketball_Property_InfoObject
from model.dto import Football_Property_Info as Football_Property_InfoObject


# os.chdir("..")
rootpath = os.getcwd()
config = config.configuration(rootpath)
try:
    connect(db=config.getconfig("DatawareHouse", "DBname"), username=config.getconfig("DatawareHouse", "Account"), password=config.getconfig("DatawareHouse", "Password"), host=config.getconfig("DatawareHouse", "FullURL"))
except ConnectionError:
    print("Could not connect to MongoDB", file=stderr)

class player_basic_data(Document):
    name_info = EmbeddedDocumentField(Name_InfoObject)
    leaguelist = ListField(ObjectIdField())
    teamlist = ListField(ObjectIdField())
    sport_type = IntField()
    logo = StringField()
    birthday = DateTimeField()
    team_info = EmbeddedDocumentField(Team_InfoObject)
    webside = StringField()
    height = StringField()
    weight = StringField()
    national_info = EmbeddedDocumentField(National_InfoObject)
    graduation = StringField()
    draft_selection = IntField()
    draft_team = StringField()
    draft_year = StringField()
    city_info = EmbeddedDocumentField(Name_InfoObject)
    property = DictField()
    status = IntField()
    shirt_number = IntField()
    referenceid = IntField()
    memo = StringField()
    update_user = StringField(max_length=50)
    update_time = DateTimeField(required=False)
    create_time = DateTimeField()

    def find(Q):
        return player_basic_data.objects(Q)

    def findcount(Q):
        return player_basic_data.objects(Q).count()

    def findfirst(Q):
        return player_basic_data.objects(Q).first()

    def findPlayerbyreferenceid(referenceid):
        return player_basic_data.objects(Q(referenceid=referenceid)).first()
import os
from utils import config
from mongoengine import *
from mongoengine.queryset.visitor import Q
from datetime import datetime
from model.dto import National_Info
from model.dto import Name_Info
from model.dto import Arena
from model.dto import Coach

# national_info = National_Info()
# arena = Arena()
# coach = Coach()


# os.chdir("..")
rootpath = os.getcwd()
config = config.configuration(rootpath)
try:
    connect(db=config.getconfig("DatawareHouse", "DBname"), username=config.getconfig("DatawareHouse", "Account"), password=config.getconfig("DatawareHouse", "Password"), host=config.getconfig("DatawareHouse", "FullURL"))
except ConnectionError:
    print("Could not connect to MongoDB", file=stderr)


class team_basic_data(Document):
    leagueidlist = ListField(ObjectIdField())
    sport_type = IntField()
    name_info = EmbeddedDocumentField(Name_Info)
    league_area = IntField()
    logo = StringField(required=False, max_length=200)
    nationalinfo = EmbeddedDocumentField(National_Info)
    isnational = IntField()
    website = StringField()
    city_en = StringField(required=True, max_length=50)
    city_zh = StringField(required=True, max_length=50)
    estableish_date = StringField(required=True, max_length=10)
    join_date = StringField(required=True, max_length=10)
    area_info = EmbeddedDocumentField(Arena)
    coach_info = EmbeddedDocumentField(Coach)
    intro = StringField(max_length=1000000, required=False)
    memo = StringField(max_length=50, required=False)
    referenceid = IntField()
    update_user = StringField(max_length=50, required=False)
    update_time = DateTimeField(required=False)
    create_time = DateTimeField()

    def find(Q):
        return team_basic_data.objects(Q)

    def findcount(Q):
        return team_basic_data.objects(Q).count()

    def findfirst(Q):
        return team_basic_data.objects(Q).first()

    def findTeamListbyObjectId(objectId):
        return team_basic_data.objects(Q(leagueidlist=objectId))

    def findTeambyreferenceId(referenceId):
        return team_basic_data.objects(Q(referenceid=referenceId)).first()
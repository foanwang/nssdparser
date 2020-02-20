import os
from utils import config
from mongoengine import *
from mongoengine.queryset.visitor import Q
from model.dto import Area

os.chdir("..")
rootpath = os.getcwd()
config = config.configuration(rootpath)
try:
    connect(db=config.getconfig("DatawareHouse", "DBname"), username=config.getconfig("DatawareHouse", "Account"), password=config.getconfig("DatawareHouse", "Password"), host=config.getconfig("DatawareHouse", "FullURL"))
except ConnectionError:
    print("Could not connect to MongoDB", file=stderr)


AreaObject = Area

class TeamDetail(EmbeddedDocument):
    Id = IntField()
    Name = StringField()
    ShortName = StringField()
    EnName = StringField()
    EstablishDate = StringField()
    JoinUnitDate = StringField()
    Area = DictField()
    City = StringField()
    Website = StringField()
    Intro = StringField()
    Arena = EmbeddedDocumentField(AreaObject)
    Retired = StringField()
    Titles = StringField()
    Photo = StringField()
    PlayerAgeAvg = StringField()

class Raw_data_Team(EmbeddedDocument):
    TeamInfo = EmbeddedDocumentField(TeamDetail)
    Players = ListField()
    Coach = DictField()

class Raw_data_Player(EmbeddedDocument):
    Id = IntField()
    Name = StringField()
    EnName = StringField()
    Birthday = StringField()
    Height = StringField()
    Weight = StringField()
    Nationality = StringField()
    FinishSchool = StringField()
    Salary = StringField()
    Club = StringField()
    Club_id = StringField()
    PreviousClub = StringField()
    PastClub =StringField()
    JoinDate = StringField()
    ClubShirtNO = StringField()
    Position = StringField()
    Glory = StringField()
    Experience = StringField()
    Note = StringField()
    Photo = StringField()

class Api_data_raw(Document):
    api_name = StringField(required=True, max_length=50)
    hash = StringField(required=True, max_length=100)
    query_parameter = StringField(required=True, max_length=50)
    source_id = StringField(required=True, max_length= 50)
    sports_type = StringField(required=True, max_length= 50)
    timestamp = FloatField()
    raw_data = DictField()
    _header = StringField()

    def find(Q):
        return Api_data_raw.objects(Q)

    def findcount(Q):
        return Api_data_raw.objects(Q).count()

apilist =['player_info', 'team_info', 'game_stat', 'getgameinfo', 'game_prediction', 'getschedulebydate']
for apiname in apilist:
    filter = Q(api_name=apiname, sports_type="basketball")
    if apiname == "team_info":
        Api_data_raw.raw_data = EmbeddedDocumentField(Raw_data_Team)
        data = Api_data_raw.find(filter)
        for doc in data:
            print(doc.raw_data)
    if apiname == "player_info":
        Api_data_raw.raw_data = EmbeddedDocumentField(Raw_data_Player)
        data = Api_data_raw.find(filter)
        for doc in data:
            print(doc.raw_data)
    if apiname == "player_info":
        Api_data_raw.raw_data = EmbeddedDocumentField(Raw_data_Player)
        data = Api_data_raw.find(filter)
        for doc in data:
            print(doc.raw_data)





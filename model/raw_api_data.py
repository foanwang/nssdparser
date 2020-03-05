import os
from utils import config
from mongoengine import *
from mongoengine.queryset.visitor import Q
from model.dto import Arena

# os.chdir("..")
rootpath = os.getcwd()
config = config.configuration(rootpath)
try:
    connect(db=config.getconfig("DatawareHouse", "DBname"), username=config.getconfig("DatawareHouse", "Account"), password=config.getconfig("DatawareHouse", "Password"), host=config.getconfig("DatawareHouse", "FullURL"))
except ConnectionError:
    print("Could not connect to MongoDB", file=stderr)

AreaObject = Arena

footballapiList=['team_detail', 'match_detail', 'season_stats', 'player_detail', 'season_list', 'match_detail_live', 'team_list', 'season_detail', 'match_even_list', 'match_lineup']
apilist = ['player_info', 'team_info', 'game_stat', 'getgameinfo', 'game_prediction', 'getschedulebydate']



class Teamdetail(EmbeddedDocument):
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

class raw_data_team(EmbeddedDocument):
    TeamInfo = EmbeddedDocumentField(Teamdetail)
    Players = ListField()
    Coach = DictField()

class raw_data_player(EmbeddedDocument):
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
    PastClub = StringField()
    JoinDate = StringField()
    ClubShirtNO = StringField()
    Position = StringField()
    Glory = StringField()
    Experience = StringField()
    Note = StringField()
    Photo = StringField()
# football  structure
# class seasonlist(EmbeddedDocument)

class raw_api_data(Document):
    api_name = StringField(required=True, max_length=50)
    match_key = StringField(required=True, max_length=50)
    source_match_id = StringField(required=True, max_length=50)
    hash = StringField(required=True, max_length=100)
    query_parameter = StringField(required=True, max_length=50)
    source_id = StringField(required=True, max_length= 50)
    sports_type = StringField(required=True, max_length= 50)
    timestamp = FloatField()
    raw_data = DictField()
    _header = StringField()

    def find(Q):
        return raw_api_data.objects(Q)

    def findcount(Q):
        return raw_api_data.objects(Q).count()

    def findfirst(Q):
        return raw_api_data.objects(Q).first()

    def findlastOrderbyDate(Q):
        return raw_api_data.objects(Q).order_by("timestamp").first()

# filter = Q(api_name="season_list", source_id="7")
# data = raw_api_data.findlastOrderbyDate(filter)
# print(data.to_json())


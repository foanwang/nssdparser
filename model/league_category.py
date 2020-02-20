import os
from utils import config
from mongoengine import *
from datetime import datetime

os.chdir("..")
rootpath = os.getcwd()
config = config.configuration(rootpath)
try:
    connect(db=config.getconfig("DatawareHouse", "DBname"), username=config.getconfig("DatawareHouse", "Account"), password=config.getconfig("DatawareHouse", "Password"), host=config.getconfig("DatawareHouse", "FullURL"))
except ConnectionError:
    print("Could not connect to MongoDB", file=stderr)

class league_category(Document):
    name_en = StringField(required=True, max_length=50)
    name_zh = StringField(required=True, max_length=50)
    sport_type = IntField()
    frequency = IntField(required=False) #1固定循環 2 不定時
    year = IntField(required=False)
    # star_time = DateTimeField(required=False)
    # end_time = DateTimeField(required=False)
    memo = StringField(required=False, max_length=100)
    update_user = StringField(required=True, max_length=50)
    update_time = DateTimeField(required=False)
    create_time = DateTimeField(required=True)

nba = league_category()
nba.name_en = "NBA"
nba.name_zh = "美国男子职业篮球联赛"
nba.sport_type = 1
nba.frequency = 1
nba.year = 0
# nba.star_time =
# nba.end_time =
nba.memo = ""
nba.update_user = ""
nba.update_time = None
nba.create_time =  datetime.now()
nba.save()


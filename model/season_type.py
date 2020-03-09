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

class season_type(Document):
    leagueid = ObjectIdField()
    sport_type = IntField()
    season_type = IntField()
    name_en = StringField(max_length=50)
    name_zh = StringField(max_length=50)
    memo = StringField()
    update_user = StringField(max_length=50)
    update_time = DateTimeField(required=False)
    create_time = DateTimeField()



NBAseason_typelist = [1, 2, 3, 4, 5, 6, 7]
NBAseasonNamelist = ["熱身賽", "一", "明星賽","季前賽", "季後賽"]

stagelist: {'1 联赛', '1 分组赛', '2 决赛', '2 1/4决赛', '2 半决赛', '2 附加赛', '1 外围赛', '2 1/8决赛'}
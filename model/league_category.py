import os
from utils import config
from mongoengine import *
import json
from datetime import datetime

# os.chdir("..")
rootpath = os.getcwd()
# print("rootpath:", rootpath)
config = config.configuration(rootpath)
try:
    connect(db=config.getconfig("DatawareHouse", "DBname"), username=config.getconfig("DatawareHouse", "Account"), password=config.getconfig("DatawareHouse", "Password"), host=config.getconfig("DatawareHouse", "FullURL"))
except ConnectionError:
    print("Could not connect to MongoDB", file=stderr)

class league_category(Document):
    name_en = StringField(required=True, max_length=50)
    name_zh = StringField(required=True, max_length=50)
    sport_type = IntField()
    frequency = IntField(required=False) #1固定循環 2特別循環
    year = IntField(required=False)
    # star_time = DateTimeField(required=False)
    # end_time = DateTimeField(required=False)
    referenceid = IntField(required=False)
    memo = StringField(required=False, max_length=100)
    update_user = StringField(required=True, max_length=50)
    update_time = DateTimeField(required=False)
    create_time = DateTimeField(required=True)

    def find(Q):
        return league_category.objects(Q)

    def findcount(Q):
        return league_category.objects(Q).count()

    def findfirst(Q):
        return league_category.objects(Q).first()

    def findleaguebysport_type(typeid):
        return league_category.objects(Q(sport_type=typeid))
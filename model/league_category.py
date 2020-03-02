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

# filter2 = Q(name_en="NBA")
# leagueobject = league_category.findfirst(filter2)
# print(leagueobject.to_json())
# for doc in leagueobject:
#     print(doc.to_json())
#     print(doc.id)
# ===============================================================================================
#   add new league for all race
# ===============================================================================================
# nba = league_category()
# nba.name_en = "NBA"
# nba.name_zh= "美国男子职业篮球联赛"
# nba.sport_type = 1
# nba.frequency = 1
# nba.year = 0
# # nba.star_time =
# # nba.end_time =
# nba.memo = ""
# nba.update_user = ""
# nba.update_time = None
# nba.create_time =  datetime.now()
# nba.save()
#
# FiGC = league_category()
# FiGC.name_en = "Italian Serie A"
# FiGC.name_zh= "意大利甲级联赛"
# FiGC.sport_type = 2
# FiGC.frequency = 1
# FiGC.year = 0
# # nba.star_time =
# # nba.end_time =
# FiGC.memo = ""
# FiGC.update_user = ""
# FiGC.update_time = None
# FiGC.create_time = datetime.now()
# FiGC.save()
#
# BLA = league_category()
# BLA.name_en= "German Bundesliga"
# BLA.name_zh = "德国甲级联赛"
# BLA.sport_type = 2
# BLA.frequency = 1
# BLA.year = 0
# # nba.star_time =
# # nba.end_time =
# BLA.memo = ""
# BLA.update_user = ""
# BLA.update_time = None
# BLA.create_time = datetime.now()
# BLA.save()
#
# CF = league_category()
# CF.name_en= "France Ligue 1"
# CF.name_zh= "法国甲级联赛"
# CF.sport_type = 2
# CF.frequency = 1
# CF.year = 0
# # nba.star_time =
# # nba.end_time =
# CF.memo = ""
# CF.update_user = ""
# CF.update_time = None
# CF.create_time = datetime.now()
# CF.save()
#
# laliga = league_category()
# laliga.name_en= "Spanish La Liga"
# laliga.name_zh= "西班牙足球甲级联赛"
# laliga.sport_type = 2
# laliga.frequency = 1
# laliga.year = 0
# # nba.star_time =
# # nba.end_time =
# laliga.memo = ""
# laliga.update_user = ""
# laliga.update_time = None
# laliga.create_time = datetime.now()
# laliga.save()
#
#
# FAPL = league_category()
# FAPL.name_en= "England Premier League"
# FAPL.name_zh= "英格兰超级联赛"
# FAPL.sport_type = 2
# FAPL.frequency = 1
# FAPL.year = 0
# # nba.star_time =
# # nba.end_time =
# FAPL.memo = ""
# FAPL.update_user = ""
# FAPL.update_time = None
# FAPL.create_time = datetime.now()
# FAPL.save()
#
# CSL = league_category()
# CSL.name_en = "CSL"
# CSL.name_zh = "中超"
# CSL.sport_type = 2
# CSL.frequency = 1
# CSL.year = 0
# # nba.star_time =
# # nba.end_time =
# CSL.memo = ""
# CSL.update_user = ""
# CSL.update_time = None
# CSL.create_time = datetime.now()
# CSL.save()
#
# CSL = league_category()
# CSL.name_en = "UEFA"
# CSL.name_zh = "欧洲国家杯"
# CSL.sport_type = 2
# CSL.frequency = 2
# CSL.year = 0
# # nba.star_time =
# # nba.end_time =
# CSL.memo = ""
# CSL.update_user = ""
# CSL.update_time = None
# CSL.create_time = datetime.now()
# CSL.save()
#
# CBA = league_category()
# CBA.name_en = "CBA"
# CBA.name_zh = "中国男子篮球职业联赛"
# CBA.sport_type = 1
# CBA.frequency = 1
# CBA.year = 0
# # nba.star_time =
# # nba.end_time =
# CBA.memo = ""
# CBA.update_user = ""
# CBA.update_time = None
# CBA.create_time = datetime.now()
# CBA.save()
#
#
#
# FIBA = league_category()
# FIBA.name_en = "FIBA"
# FIBA.name_zh = "世界篮球杯"
# FIBA.sport_type = 1
# FIBA.frequency = 2
# FIBA.year = 0
# # nba.star_time =
# # nba.end_time =
# FIBA.memo = ""
# FIBA.update_user = ""
# FIBA.update_time = None
# FIBA.create_time = datetime.now()
# FIBA.save()

# UEFA = league_category()
# UEFA.name_en = "UEFA European Championship"
# UEFA.name_zh = "欧洲国家杯"
# UEFA.sport_type = 2
# UEFA.frequency = 2
# UEFA.year = 0
# # nba.star_time =
# # nba.end_time =
# UEFA.memo = ""
# UEFA.update_user = ""
# UEFA.update_time = None
# UEFA.create_time = datetime.now()
# UEFA.save()
#
# CSL = league_category()
# CSL.name_en = "Chinese Super League"
# CSL.name_zh = "中國超級聯賽"
# CSL.sport_type = 2
# CSL.frequency = 2
# CSL.year = 0
# # nba.star_time =
# # nba.end_time =
# CSL.memo = ""
# CSL.update_user = ""
# CSL.update_time = None
# CSL.create_time = datetime.now()
# CSL.save()
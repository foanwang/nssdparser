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

class team_bb_history_details(EmbeddedDocument):
    rank = IntField() #總排名
    division_rank = IntField()#聯盟排名
    total_matchs = IntField()
    won_rate = FloatField()
    home_win = IntField()
    home_lost = IntField()
    away_win = IntField()
    away_lost = IntField()
    minutes = IntField()
    total_points = IntField()
    fields_shout_count = IntField()
    fields_point = IntField()
    free_throw_show = IntField()
    free_throw_show_count = IntField()
    three_point_show_goal = IntField()
    off_reb = IntField()
    def_reb = IntField()
    assists = IntField()
    steal = IntField()
    fouls = IntField()
    turnover = IntField()

class team_fb_history_details(EmbeddedDocument):
    matches = IntField()
    goals = IntField()
    goals_against = IntField()
    penalty = FloatField()
    assists = IntField()
    home_lost = IntField()
    red_cards = IntField()
    yellow_cards = IntField()
    shots = IntField()
    shots_on_target = IntField()
    clearances = IntField()
    tackles = IntField()
    interceptions = IntField()
    key_passes = IntField()
    crosses = IntField()
    crosses_accuracy = IntField()
    fouls = IntField()

class team_event_log(Document):
    teamid = StringField()
    year = IntField()
    season_type = IntField()
    sporttype = IntField()
    detail = DictField()
    update_user = StringField(max_length=50)
    update_time = DateTimeField(required=False)
    create_time = DateTimeField()

    def getTeameEvenLog(self):
        if team_event_log.sporttype==1:
            team_event_log.detail = EmbeddedDocumentField(team_bb_history_details)
        else:
            team_event_log.detail = EmbeddedDocumentField(team_fb_history_details)
        return self



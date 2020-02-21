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

class basketball_player_history(EmbeddedDocument):
    game = IntField()
    total_point = IntField()
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

class football_player_history(EmbeddedDocument):
    rating = FloatingPointError()
    matches = IntField()
    first = IntField()
    goal = IntField()
    penalty = IntField()
    assists = IntField()
    minutes_played = IntField()
    red_cards = IntField()
    yellow_cards = IntField()
    shots = IntField()
    shots_on_target = IntField()
    dribble = IntField()
    dribble_success = IntField()
    clearance = IntField()
    blocked_shots = IntField()
    interceptions = IntField()
    tackles = IntField()
    passes = IntField()
    passes_accuracy = IntField()
    key_passes =IntField()
    crosses = IntField()
    crosses_accuracy = IntField()
    long_ball = IntField()
    long_ball_accuracy = IntField()
    duels = IntField()
    duels_won = IntField()
    dispossessed = IntField()
    fouls = IntField()
    was_fouled = IntField()
    saves = IntField()
    punches = IntField()
    runs_out = IntField()
    runs_out_success = IntField()

class player_history(Document):
    leagueid = StringField()
    teamid = StringField()
    year = IntField()
    seasontype = IntField()
    detail = EmbeddedDocumentField()
    rank = IntField()
    update_user = StringField(max_length=50)
    update_time = DateTimeField(required=False)
    create_time = DateTimeField()

    def find(Q):
        return position.objects(Q)

    def findcount(Q):
        return position.objects(Q).count()
from mongoengine import *

class National_Info(EmbeddedDocument):
    national_flag = StringField()
    national_name_en = StringField()
    national_name_zh = StringField()

class Name_Info(EmbeddedDocument):
    short_en = StringField()
    short_zh = StringField()
    name_en = StringField()
    name_zh = StringField()


class Arena(EmbeddedDocument):
    name_en = StringField()
    name_zh = StringField()
    address_en = StringField()
    address_zh = StringField()
    capacity = StringField()
    opened = StringField()
    ticketPrice = StringField()

class Coach(EmbeddedDocument):
    name_en = StringField()
    name_zh = StringField()
    photo_link = StringField()

class Team_Info(EmbeddedDocument):
    teamid = ObjectIdField()
    short_en = StringField()
    short_zh = StringField()
    name_en = StringField()
    name_zh = StringField()
    logo = StringField()

class National_Info(EmbeddedDocument):
    national_flag = StringField()
    national_name_en = StringField()
    national_name_zh = StringField()

class Match_Team_Info(EmbeddedDocument):
    teamid = StringField()
    name_info = EmbeddedDocumentField(EmbeddedDocument)
    flag = StringField()
    logo = StringField()

class Match_Playerd_Recrod(EmbeddedDocument):
    playerid = ObjectIdField()
    nameinfo = EmbeddedDocumentListField(Name_Info)
    logo = StringField()
    propertydata = DictField()
    score = IntField()
    start = BooleanField()

class Basketball_match_record(EmbeddedDocument):
   firstscore = IntField()
   secondscore = IntField()
   thirdscore = IntField()
   fourthtscore = IntField()
   overtime = ListField()
   turnover =IntField()
   fouls = IntField()
   steal = IntField()
   assists = IntField()
   def_reb = IntField()
   off_reb = IntField()
   three_point_shot_count = IntField()
   three_point_shot_goal = IntField()
   free_throw_shot = IntField()
   free_throw_shot_count = IntField()
   field_goal = IntField()
   field_shot_count =IntField()

class Football_match_record(EmbeddedDocument):
   usual_score = IntField()
   half_score = IntField()
   red_cards = IntField()
   yellow_cards = IntField()
   corner = IntField()
   overtime = IntField()
   penalty = IntField()

class Basketball_Property_Info():
    def __init__(self, position_en, position_zh):
        self.position_en = position_en
        self.position_zh = position_zh

class Football_Property_Info():
    def __init__(self, position_en, position_zh, positions_en, positions_zh, sec_poistions_en, sec_poistions_zh, preferred_foot, ability, characteristics):
        self.position_en = position_en
        self.position_zh = position_zh
        self.positions_en = position_en
        self.positions_zh = position_zh
        self.sec_poistions_en = sec_poistions_en
        self.sec_poistions_zh = sec_poistions_zh
        self.preferred_foot = preferred_foot# 1左腳 2右腳
        self.ability = ability
        self.characteristics = characteristics
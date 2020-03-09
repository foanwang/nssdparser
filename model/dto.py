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
    name_info = EmbeddedDocumentField(Name_Info)
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


class player_bb_history_details():
    def __init__(self, rank, division_rank, total_matchs, won_rate, home_win, home_lost, away_win, away_lost, minutes, total_points, fields_shout_count, fields_point,
                 free_throw_show, free_throw_show_count, three_point_show_goal, off_reb, def_reb, assists, steal, fouls, turnover):
        self.rank = rank  # 總排名
        self.division_rank = division_rank # 聯盟排名
        self.total_matchs = total_matchs
        self.won_rate = won_rate
        self.home_win = home_win
        self.home_lost = home_lost
        self.away_win = away_win
        self.away_lost = away_lost
        self.minutes = minutes
        self.total_points = total_points
        self.fields_shout_count = fields_shout_count
        self.fields_point = fields_point
        self.free_throw_show = free_throw_show
        self.free_throw_show_count = free_throw_show_count
        self.three_point_show_goal = three_point_show_goal
        self.off_reb = off_reb
        self.def_reb = def_reb
        self.assists = assists
        self.steal = steal
        self.fouls = fouls
        self.turnover = turnover

class player_fb_history_details():
    def __init__(self, matches, goals, goals_against, penalty, assists, red_cards, yellow_cards, shots, shots_on_target,
                 dribble, dribble_succ, clearances, blocked_shots, tackles, passes, passes_accuracy, interceptions, key_passes, crosses,
                 crosses_accuracy, duels, duels_won, long_balls,long_balls_accuracy, fouls, was_fouled):
        self.matches = matches  #比賽場次
        self.goals = goals  #進球
        self.goals_against = goals_against  #失球
        self.penalty = penalty  #點球
        self.assists = assists  #助攻
        self.red_cards = red_cards  #紅牌
        self.yellow_cards = yellow_cards    #黃牌

        self.shots = shots  #射門
        self.shots_on_target = shots_on_target  #射正
        self.dribble = dribble  #過人
        self.dribble_succ = dribble_succ    #過人成功
        self.clearances = clearances    #解圍
        self.blocked_shots = blocked_shots  #有效阻擋
        self.interceptions = interceptions  #截斷
        self.tackles = tackles  #搶斷

        self.passes = passes    #傳球
        self.passes_accuracy = passes_accuracy  #精準傳球
        self.key_passes = key_passes    #關鍵傳球
        self.crosses = crosses  #傳中球
        self.crosses_accuracy = crosses_accuracy    #傳中球成功
        self.long_balls = long_balls    #長傳
        self.long_balls_accuracy = long_balls_accuracy #長傳成功

        self.duels = duels  #一對一拼搶
        self.duels_won = duels_won  #一對一乒搶成功
        self.fouls = fouls  #犯規
        self.was_fouled = was_fouled    #被犯規

class team_fb_history_details():
    def __init__(self, matches, goals, goals_against, penalty, assists, red_cards, yellow_cards, shots, shots_on_target,
                 dribble, dribble_succ, clearances, blocked_shots, tackles, passes, passes_accuracy, interceptions, key_passes, crosses,
                 crosses_accuracy, duels, duels_won, long_balls,long_balls_accuracy, fouls, was_fouled):
        self.matches = matches  #比賽場次
        self.goals = goals  #進球
        self.goals_against = goals_against  #失球
        self.penalty = penalty  #點球
        self.assists = assists  #助攻
        self.red_cards = red_cards  #紅牌
        self.yellow_cards = yellow_cards    #黃牌

        self.shots = shots  #射門
        self.shots_on_target = shots_on_target  #射正
        self.dribble = dribble  #過人
        self.dribble_succ = dribble_succ    #過人成功
        self.clearances = clearances    #解圍
        self.blocked_shots = blocked_shots  #有效阻擋
        self.interceptions = interceptions  #截斷
        self.tackles = tackles  #搶斷

        self.passes = passes    #傳球
        self.passes_accuracy = passes_accuracy  #精準傳球
        self.key_passes = key_passes    #關鍵傳球
        self.crosses = crosses  #傳中球
        self.crosses_accuracy = crosses_accuracy    #傳中球成功
        self.long_balls = long_balls    #長傳
        self.long_balls_accuracy = long_balls_accuracy #長傳成功

        self.duels = duels  #一對一拼搶
        self.duels_won = duels_won  #一對一乒搶成功
        self.fouls = fouls  #犯規
        self.was_fouled = was_fouled    #被犯規

class Basketball_Property_Info():
    def __init__(self, position_en, position_zh):
        self.position_en = position_en
        self.position_zh = position_zh

class Football_Property_Info():
    def __init__(self, position_en, position_zh, positions_en, positions_zh, sec_poistions_en, sec_poistions_zh, preferred_foot, ability, characteristics):
        self.position_en = position_en
        self.position_zh = position_zh
        self.positions_en = positions_en
        self.positions_zh = positions_zh
        self.sec_poistions_en = sec_poistions_en
        self.sec_poistions_zh = sec_poistions_zh
        self.preferred_foot = preferred_foot# 1左腳 2右腳
        self.ability = ability
        self.characteristics = characteristics
from model.league_category import league_category as league
from datetime import datetime
from model.raw_api_data import *
from mongoengine.queryset.visitor import Q

Leaguelist = {45, 82, 108, 120, 129, 142, 542}

def FootballLeagueParser():
    leaguedfilter = Q(api_name="season_list", source_id="7")
    lastleaguedata = raw_api_data.findlastOrderbyDate(leaguedfilter)
    competitionlist = lastleaguedata.raw_data.get("competitions")
    for leagueid in Leaguelist:
        # print("leagueid:", leagueid)
        for doc in competitionlist:
            if doc.get('id') == leagueid:
                # print(doc.get('id'))
                newleague = league()
                newleague.name_en = doc.get('name_en')
                newleague.name_zh= doc.get('name_zh')
                newleague.sport_type = 2
                newleague.frequency = 1
                newleague.year = 0
                newleague.memo = ""
                newleague.update_user = ""
                newleague.update_time = None
                newleague.referenceid = leagueid
                newleague.create_time = datetime.now()
                checkdatafilter = Q(name_en=doc.get('name_en'))
                if league.findcount(checkdatafilter) <= 0:
                    newleague.save()

def BasketballLeagueParser():
    nba = league()
    nba.name_en = "NBA"
    nba.name_zh= "美国男子职业篮球联赛"
    nba.sport_type = 1
    nba.frequency = 1
    nba.year = 0
    nba.referenceid = 0
    nba.memo = ""
    nba.update_user = ""
    nba.update_time = None
    nba.create_time = datetime.now()
    checkdatafilter = Q(name_en=nba.name_en)
    if league.findcount(checkdatafilter) <= 0:
        nba.save()

    CBA = league()
    CBA.name_en = "CBA"
    CBA.name_zh = "中国男子篮球职业联赛"
    CBA.sport_type = 1
    CBA.frequency = 1
    CBA.year = 0
    CBA.referenceid = 0
    CBA.memo = ""
    CBA.update_user = ""
    CBA.update_time = None
    CBA.create_time = datetime.now()
    checkdatafilter = Q(name_en=CBA.name_en)
    if league.findcount(checkdatafilter) <= 0:
        CBA.save()

    FIBA = league()
    FIBA.name_en = "FIBA"
    FIBA.name_zh = "世界篮球杯"
    FIBA.sport_type = 1
    FIBA.frequency = 2
    FIBA.year = 0
    FIBA.referenceid = 0;
    FIBA.memo = ""
    FIBA.update_user = ""
    FIBA.update_time = None
    FIBA.create_time = datetime.now()
    checkdatafilter = Q(name_en=FIBA.name_en)
    if league.findcount(checkdatafilter) <= 0:
        FIBA.save()


# BasketballLeagueParser()
FootballLeagueParser()
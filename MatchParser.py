from datetime import datetime

from mongoengine import *
from mongoengine.queryset.visitor import Q
import json
from model.team_basic_data import team_basic_data as teambasic
from model.league_category import league_category as league
from model.match import match
from model.dto import *
from model.raw_api_data import *


HomeTeamInfo = Match_Team_Info()
AwayTemainfo = Match_Team_Info()

def parserHomeTeamInfo(teamid, nameinfo, logo):
    HomeTeamInfo.teamid = teamid
    HomeTeamInfo.name_info = nameinfo
    HomeTeamInfo.logo = logo
    return HomeTeamInfo

def parserAwayTemainfo(teamid, nameinfo, logo):
    AwayTemainfo.teamid = teamid
    AwayTemainfo.name_info = nameinfo
    AwayTemainfo.logo = logo
    return AwayTemainfo

def FootballHistoryParser():
    # get our league list
    leaguedfilter = Q(sport_type=2)
    referenceIdList = list()
    leaguelist = league.find(leaguedfilter)
    for doc in leaguelist:
        referenceIdList.append(doc.referenceid)

    # get each league team list from nami
    leagueteamdic = dict()
    leaguefilter = Q(api_name="season_list")
    lastleaguedata = raw_api_data.findlastOrderbyDate(leaguefilter)
    competitionlist = lastleaguedata.raw_data.get("competitions")
    # print("competitionlist", competitionlist)
    for leagueid in referenceIdList:
        print("leagueid", leagueid)
        for doc in competitionlist:
            # print("doc:", doc)
            # print("doc id:", doc.get('id'), "leagueid:", leagueid)
            if doc.get('id') == int(leagueid):
                print("doc id:", doc.get('id'), "leagueid:", leagueid)
                if doc.get("seasons")[0] is None:
                    print(leagueid, "is not data on season_list")
                    continue

                # here need change to all season
                seasonid = doc.get("seasons")[0].get("id")
                seasonyear =doc.get("seasons")[0].get("seasons")
                print("seasonid:", seasonid)

                leaguefilter = Q(api_name="season_detail", query_parameter=str(seasonid))
                seasondata = raw_api_data.findfirst(leaguefilter)
                print('seasondata:', seasondata.to_json())
                RawMatchList = seasondata.raw_data.get("matches")
                for rawmatch in RawMatchList:
                    # print("rawmatch:",rawmatch)
                    hometeam = teambasic.findTeambyreferenceId(rawmatch.get("home_team_id"))
                    if hometeam is not None:
                        parserHomeTeamInfo(hometeam.id, hometeam.name_info, hometeam.logo)
                    awayteam = teambasic.findTeambyreferenceId(rawmatch.get("away_team_id"))
                    if awayteam is not None:
                        parserAwayTemainfo(awayteam.id, awayteam.name_info, awayteam.logo)
                    print("id:",rawmatch.get("id"))
                    leaguefilter = Q(api_name="match_lineup", query_parameter=rawmatch.get("id"))
                    matchlineup = raw_api_data.findfirst(leaguefilter)
                    print("matchlineup:", matchlineup)
                    # match(
                    #     leagueid=leagueid, year=seasonyear,
                    #     race_no=IntField(), sport_type=2,
                    #     season_type= (),
                    #     home_info=HomeTeamInfo,
                    #     away_info=AwayTemainfo,
                    #     arena_data=None,
                    #     status=IntField(),
                    #     match_time=rawmatch.get("match_time"),
                    #     referenceId=rawmatch.get("id"),
                    #     update_user=None,
                    #     update_time=None,
                    #     create_time=datetime.now()
                    # ).save()
                    #


FootballHistoryParser()
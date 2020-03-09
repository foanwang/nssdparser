from datetime import datetime

from mongoengine import *
from mongoengine.queryset.visitor import Q
import json

from model.league_category import league_category as league
from model.team_basic_data import team_basic_data as teambasic
from model.team_history import team_history
from model.dto import *
from model.raw_api_data import *

def football_team_history_parser():
    # get our league list
    leaguedfilter = Q(sport_type=2)
    referenceIddict = dict()
    leaguelist = league.find(leaguedfilter)
    for doc in leaguelist:
        referenceIddict[doc.id] = doc.referenceid

    # get each league team list from nami
    leaguefilter = Q(api_name="season_list")
    lastleaguedata = raw_api_data.findlastOrderbyDate(leaguefilter)
    competitionlist = lastleaguedata.raw_data.get("competitions")
    # print("competitionlist", competitionlist)
    for key in referenceIddict:
        print("leagueid", key)
        print("league_refernceid", referenceIddict[key])
        for doc in competitionlist:
            # print("doc:", doc)
            # print("doc id:", doc.get('id'), "leagueid:", leagueid)
            if doc.get('id') == int(referenceIddict[key]):
                print("doc id:", doc.get('id'), "leagueid:",  referenceIddict[key])
                if doc.get("seasons")[0] is None:
                    print(referenceIddict[key], "is not data on season_list")
                    continue

                #here need change to all season
                seasonid = doc.get("seasons")[0].get('id')
                print("seasonid:", doc.get("seasons")[0].get('id'))

                leaguefilter = Q(api_name="season_stats", query_parameter=str(seasonid))
                rawseasonstats = raw_api_data.findfirst(leaguefilter)
                if rawseasonstats == None:
                    print("can't find season stats data, query id:", str(seasonid))
                    continue
                # print('rawseasonstats:', rawseasonstats.raw_data)


                rawteamstatslist = rawseasonstats.raw_data.get("teams_stats")
                for rawteamstats in rawteamstatslist:
                    # print("rawteamstats:", rawteamstats)
                    teamdata = teambasic.findTeambyreferenceId(rawteamstats.get("team").get("id"))

                    if (team_history.findTeamHistoryByLeagueandTeamidandYear(key, teamdata.id, doc.get("seasons")[0].get('season')) != None):
                        print("leagueid:", key , " team id:", teamdata.id, " year:", doc.get("seasons")[0].get('season'), " data is exist")
                        continue

                    # print("teamid:", teamdata)
                    # print("matches:", rawteamstats.get("matches"))
                    detail = team_fb_history_details(rawteamstats.get("matches"),
                                                     rawteamstats.get("goals"),
                                                     rawteamstats.get("goals_against"),
                                                     rawteamstats.get("penalty"),
                                                     rawteamstats.get("assists"),
                                                     rawteamstats.get("red_cards"),
                                                     rawteamstats.get("yellow_cards"),
                                                     rawteamstats.get("shots"),
                                                     rawteamstats.get("shots_on_target"),
                                                     rawteamstats.get("dribble"),
                                                     rawteamstats.get("dribble_succ"),
                                                     rawteamstats.get("clearances"),
                                                     rawteamstats.get("blocked_shots"),
                                                     rawteamstats.get("tackles"),
                                                     rawteamstats.get("passes"),
                                                     rawteamstats.get("passes_accuracy"),
                                                     rawteamstats.get("interceptions"),
                                                     rawteamstats.get("key_passes"),
                                                     rawteamstats.get("crosses"),
                                                     rawteamstats.get("crosses_accuracy"),
                                                     rawteamstats.get("duels"),
                                                     rawteamstats.get("duels_won"),
                                                     rawteamstats.get("long_balls"),
                                                     rawteamstats.get("long_balls_accuracy"),
                                                     rawteamstats.get("fouls"),
                                                     rawteamstats.get("was_fouled")
                                                     )
                    # print("detail:",detail.__dict__)
                    team_history(
                        leagueid = key,
                        teamid = teamdata.id,
                        year = doc.get("seasons")[0].get('season'),
                        season_type = None,
                        sport_type = 2,
                        detail = detail.__dict__,
                        update_user = None,
                        update_time = None,
                        create_time = datetime.now()
                    ).save()


def test():
    stagelist = set()
    seasondetailfilter = Q(api_name="season_detail")
    seasondetaillist = raw_api_data.find(seasondetailfilter)
    for seasondetail in seasondetaillist:
        # print("seasondetail:", seasondetail)
        for seasonstage in seasondetail.raw_data.get("stages"):
            # print('seasondetail:', seasondetail.raw_data)
            stage = str(seasonstage.get("mode"))+" "+seasonstage.get("name_zh")
            stagelist.add(stage)
    print("stagelist:", stagelist)

# test()
football_team_history_parser()
from datetime import datetime

from mongoengine import *
from mongoengine.queryset.visitor import Q
import json
from model.position import position
from model.team_basic_data import team_basic_data as teambasic
from model.league_category import league_category as league
from model.player_basic_data import player_basic_data as playerbasic
from model.dto import *
from model.raw_api_data import *


nameinfo = Name_Info()
nationalinfo = National_Info()
teaminfo = Team_Info()


def parsernameinfo(name_en, name_zh, short_en, short_zh):
    nameinfo.name_en = name_en
    nameinfo.name_zh = name_zh
    nameinfo.short_en = short_en
    nameinfo.short_zh = short_zh
    return nameinfo

def parserteaminfo(teamid, short_en, short_zh, name_en, name_zh,  logo):
    teaminfo.teamid = teamid
    teaminfo.short_en = short_en
    teaminfo.short_zh = short_zh
    teaminfo.name_en = name_en
    teaminfo.name_zh = name_zh
    teaminfo.logo = logo
    return teaminfo

def parsernationalinfo(national_flag, national_name_en, national_name_zh):
    nationalinfo.national_flag = national_flag
    nationalinfo.national_name_en = national_name_en
    nationalinfo.national_name_zh = national_name_zh
    return nationalinfo



def basketballplayerparser():
    leaguelist = league.findleaguebysport_type(1)
    for leaguedata in leaguelist:
        print("leaguedata:", leaguedata.id)

        teamlist = teambasic.findTeamListbyObjectId(leaguedata.id)

        # get team player data
        for team in teamlist:
            print("team:", team.to_json())
            teamrawdatafilter = Q(api_name="team_info", query_parameter=str(team.referenceid))
            rawteamdata = raw_api_data.findfirst(teamrawdatafilter)

            # print(rawteamdata.raw_data.get("Players"))
            for player in rawteamdata.raw_data.get("Players"):
                print("id", player.get('Id'), " logo:", player.get("logo"))
                newdbplayfilter = Q(referenceid= player.get('Id'))
                newdblayer = playerbasic.findfirst(newdbplayfilter)
                # check player is exist on new db
                if newdblayer is None:
                    print("new player")
                    # get raw player data
                    rawdataplayerfilter = Q(api_name="player_info", query_parameter=str(player.get('Id')))
                    rawdataplayerdata = raw_api_data.findfirst(rawdataplayerfilter)
                    if rawdataplayerdata is not None:
                        leaguelist = list()
                        leaguelist.append(leaguedata.id)
                        logo = None
                        if player.get("logo") is not None:
                            logo = player.get("logo")

                        teamlist = list()
                        teamlist.append(team.id)

                        parsernameinfo(rawdataplayerdata.raw_data.get("EnName"),
                                       rawdataplayerdata.raw_data.get("Name"),
                                       None, None)
                        # print("Team name:", team.name_info.short_en, team.name_info.short_zh, team.name_info.name_en,team.name_info.name_zh )
                        parserteaminfo(team.id, "", team.name_info.short_zh, team.name_info.name_en, team.name_info.name_zh, team.logo)
                        # print("teaminfo", teaminfo.to_json())

                        parsernationalinfo(None, None, rawdataplayerdata.raw_data.get("Nationality"))

                        graduation = rawdataplayerdata.raw_data.get("FinishSchool")

                        property = None
                        positionfilter = Q(name=rawdataplayerdata.raw_data.get("Position"))
                        positiondata = position.findfirst(positionfilter)
                        # print("pos", positiondata.abbreviation, positiondata.name)

                        if positiondata is not None:
                            bpi = Basketball_Property_Info(positiondata.abbreviation, positiondata.name)
                            property = bpi.__dict__
                            print(bpi.__dict__)

                        shirt_number = None
                        if rawdataplayerdata.raw_data.get("ClubShirtNo")!= "    ":
                            shirt_number = rawdataplayerdata.raw_data.get("ClubShirtNo")

                        playerbasic(
                            name_info=nameinfo,  leaguelist=leaguelist, teamlist=teamlist,
                            sport_type=1, logo=logo,
                            birthday=rawdataplayerdata.raw_data.get("Birthday"), team_info=teaminfo,
                            webside=None, height=rawdataplayerdata.raw_data.get("Height"),
                            weight=rawdataplayerdata.raw_data.get("Weight"),  national_info=nationalinfo,
                            graduation=graduation, draft_selection=None,
                            draft_team=None, draft_year=None, city_info=None, property=property,
                            shirt_number= shirt_number,
                            status=1,
                            memo=rawdataplayerdata.raw_data.get("Note"),
                            referenceid=player.get('Id'),
                            update_user=None,
                            update_time=None,
                            create_time=datetime.now()
                        ).save()
                else:
                    print("old player")
                    print(" leaguedata.id :", leaguedata.id )
                    if leaguedata.id not in newdblayer.leaguelist:
                        newdblayer.leaguelist.append(leaguedata.id)
                        print(" newdblayer.leaguelist:", newdblayer.leaguelist)
                    if rawteamdata.id not in newdblayer.teamlist:
                        newdblayer.teamlist.append(team.id)
                    newdblayer.save()




def footballplayerparser():
    leaguelist = league.findleaguebysport_type(2)
    for leaguedata in leaguelist:
        print(leaguedata.name_zh)
        #get team list by leaggue
        teamlist = teambasic.findTeamListbyObjectId(leaguedata.id)
        # get player id from team on raw data
        for teamdata in teamlist:
            teamreferenceid = teamdata.referenceid
            teamrawdatafilter = Q(api_name="team_detail", query_parameter=str(teamreferenceid))
            rawteamdata = raw_api_data.findfirst(teamrawdatafilter)

            if rawteamdata is None:
                print("can't find team ", teamdata.name_info.short_en)
                continue

            # get playerdetail on raw data
            for rawplayer in rawteamdata.raw_data.get("players"):
                # print("rawplayer:", rawplayer)
                rawplayerid = rawplayer.get("player").get('id')
                print("rawplayerid:", rawplayerid)

                rawplayerdetailfilter = Q(api_name="player_detail", query_parameter=str(rawplayerid))
                rawplayerdetaildata = raw_api_data.findfirst(rawplayerdetailfilter)

                if rawplayerdetaildata is None:
                    print("can't find rawplayerdetaildata ", "rawplayerid:", rawplayerid)
                    continue

                # check new db player data is exist
                player = playerbasic.findplayerbyreferenceid(rawplayerid)
                if player is None:
                    print("new player")

                    leaguelist = list()
                    # print("leaguedata.id:", leaguedata.id)
                    leaguelist.append(leaguedata.id)

                    teamlist = list()
                    teamlist.append(teamdata.id)

                    logo = None
                    if rawplayer.get("logo") is not None:
                        logo = rawplayer.get("logo")

                    parsernameinfo(rawplayer.get("player").get("name_en"),
                                   rawplayer.get("player").get("name_zh"),
                                   None, None)

                    birthday = None
                    if rawplayerdetaildata.raw_data.get('birthday') is not None:
                        birthday = datetime.fromtimestamp(rawplayerdetaildata.raw_data.get('birthday'))

                    # print("Team name:", team.name_info.short_en, team.name_info.short_zh, team.name_info.name_en,team.name_info.name_zh )
                    parserteaminfo(teamdata.id, "", teamdata.name_info.short_zh, teamdata.name_info.name_en, teamdata.name_info.name_zh,
                                   teamdata.logo)
                    # print("teaminfo", teaminfo.to_json())

                    parsernationalinfo(None, None, rawplayerdetaildata.raw_data.get("nationality"))

                    graduation = None

                    property = None

                    position_en = None
                    position_zh = None
                    positions_en = None
                    positions_zh = None
                    sec_positions_en = None
                    sec_positions_zh = None

                    if rawplayer.get("position") !="":
                        positiondata = position.findPositionByAbbreviation(rawplayer.get("position"))
                        print("positiondata:", positiondata.abbreviation, positiondata.name)
                    else:
                        continue
                    position_en = positiondata.abbreviation
                    position_zh = positiondata.name
                    # print("postion", position_en, position_zh)


                    if len(rawplayerdetaildata.raw_data.get('positions')) == 0:
                        continue

                    positions = position.findPositionByAbbreviation(rawplayerdetaildata.raw_data.get('positions')[0])
                    positions_en = positions.abbreviation
                    positions_zh = positions.name
                    # print("pos1", positions_en, positions_zh)

                    if len(rawplayerdetaildata.raw_data.get('positions')[1])== 0:
                        # print("rawplayerdetaildata.raw_data.get('positions')[1] is None")
                        continue

                    sec_positions = position.findPositionByAbbreviation(rawplayerdetaildata.raw_data.get('positions')[1][0])
                    sec_positions_en = sec_positions.abbreviation
                    sec_positions_zh = sec_positions.name
                    # print("pos2", sec_positions_en, sec_positions_zh)

                    fpi = Football_Property_Info(position_en, position_zh, positions_en, positions_zh, sec_positions_en, sec_positions_zh, rawplayerdetaildata.raw_data.get("preferred_foot"), rawplayerdetaildata.raw_data.get("ability"), rawplayerdetaildata.raw_data.get("characteristics"))
                    property = fpi.__dict__
                    # print(fpi.__dict__)

                    shirt_number = None
                    if rawplayer.get("shirt_number") != None:
                        shirt_number = rawplayer.get("shirt_number")
                        # print("NO:", rawplayer.get("shirt_number"))

                    playerbasic(
                        name_info=nameinfo, leaguelist=leaguelist, teamlist = teamlist,
                        sport_type=2, logo=logo,
                        birthday=birthday, team_info=teaminfo,
                        webside=None, height=str(rawplayerdetaildata.raw_data.get("height")),
                        weight=str(rawplayerdetaildata.raw_data.get("weight")), national_info=nationalinfo,
                        graduation=graduation, draft_selection=None,
                        draft_team=None, draft_year=None, city_info=None, property=property,
                        shirt_number=shirt_number,
                        status=1,
                        memo=None,
                        referenceid=rawplayerid,
                        update_user=None,
                        update_time=None,
                        create_time=datetime.now()
                    ).save()
                else:
                    # if db already have data on new db, get leaguelist check league is on the list, if is new league , add it and save
                    print("old player")
                    # print("leaguedata.id:", leaguedata.id)
                    # print("player.leagueidlist:", player.leaguelist)
                    if leaguedata.id not in player.leaguelist:
                        player.leaguelist.append(leaguedata.id)
                        print(" player.leaguelist:",  player.leaguelist)
                    if teamdata.id not in player.teamlist:
                        player.teamlist.append(teamdata.id)
                    player.save()
    print("=================league finish===================================")


# footballplayerparser()
basketballplayerparser()
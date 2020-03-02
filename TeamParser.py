from model.team_basic_data import team_basic_data as teambasic
from model.league_category import league_category as league
from model.sport_type import sport_type as sporttype
from datetime import datetime
from model.dto import *
from model.raw_api_data import *
from mongoengine import *
from mongoengine.queryset.visitor import Q

nameinfo = Name_Info()
nationalinfo = National_Info()
arena = Arena()
coach =Coach()

apilist = ['player_info', 'team_info', 'game_stat', 'getgameinfo', 'game_prediction', 'getschedulebydate']
def parsernameinfo(name_en, name_zh, short_en, short_zh):
    nameinfo.name_en = name_en
    nameinfo.name_zh = name_zh
    nameinfo.short_en = short_en
    nameinfo.short_zh = short_zh
    return nameinfo

def parsernationalinfo(national_flag, national_name_en, national_name_zh):
    nationalinfo.national_flag = national_flag
    nationalinfo.national_name_en = national_name_en
    nationalinfo.national_name_zh = national_name_zh
    return nationalinfo

def parserarena(Name_en, Name_zh, Address_en, Address_zh, Capacity, Opened, TicketPrice):
    arena.Name_en = Name_en
    arena.Name_zh = Name_zh
    arena.Address_en = Address_en
    arena.Address_zh = Address_zh
    arena.Capacity = Capacity
    arena.Opened = Opened
    arena.TicketPrice = TicketPrice
    return arena

def parsercoach(name_en, name_zh, photo_link):
    coach.name_en = name_en
    coach.name_zh = name_zh
    coach.photo_link = photo_link
    return coach

def BasetballTeamparser():
    for apiname in apilist:
        filter = Q(api_name=apiname, sports_type="basketball")
        # parser NBA Team
        if apiname == "team_info":
            for doc in raw_api_data.objects(filter):
                checkreferencefilter = Q(referenceid=doc.raw_data.get("TeamInfo").get("Id"))
                # check referenceid is exist on db or not
                if teambasic.findfirst(checkreferencefilter) == None:
                    # NBA Data
                    if doc.raw_data.get("TeamInfo").get("Id") < 100:
                        leaguefilter = Q(name_en="NBA")
                        leagueidList = set()
                        leagueid = league.findfirst(leaguefilter).id
                        leagueidList.add(leagueid)
                        parsernameinfo(doc.raw_data.get("TeamInfo").get("EnName"),
                                       doc.raw_data.get("TeamInfo").get("Name"), None,
                                       doc.raw_data.get("TeamInfo").get("ShortName"))
                        parsernationalinfo(None, None, doc.raw_data.get("TeamInfo").get("Area"))
                        parserarena(None, doc.raw_data.get("TeamInfo").get("Arena").get("Name"), None,
                                    doc.raw_data.get("TeamInfo").get("Arena").get("Address"),
                                    doc.raw_data.get("TeamInfo").get("Arena").get("Capacity"),
                                    doc.raw_data.get("TeamInfo").get("Arena").get("Opened"),
                                    doc.raw_data.get("TeamInfo").get("Arena").get("TicketPrice"))
                        leaguelist = list()
                        leaguelist.append(leagueid)
                        teambasic(leagueid=leaguelist, sport_type=1, name_info=nameinfo,
                                  league_area=0, logo=doc.raw_data.get("TeamInfo").get("Photo"),
                                  nationalinfo=nationalinfo,
                                  city_en="", city_zh=doc.raw_data.get("TeamInfo").get("City"),
                                  estableish_date=doc.raw_data.get("TeamInfo").get("EstablishDate"),
                                  join_date=doc.raw_data.get("TeamInfo").get("JoinUnitDate"),
                                  area_info=arena, coach_info=None,
                                  intro=doc.raw_data.get("TeamInfo").get("Intro"), update_user=None,
                                  referenceid=doc.raw_data.get("TeamInfo").get("Id"),
                                  create_time=datetime.now()).save()
                    else:
                        # FIBA data
                        if doc.raw_data.get("TeamInfo").get("ShortName") == "":
                            leaguefilter = Q(name_en="FIBA")
                            leagueidList = set()
                            leagueid = league.findfirst(leaguefilter).id
                            leagueidList.add(leagueid)
                            parsernameinfo(doc.raw_data.get("TeamInfo").get("EnName"),
                                           doc.raw_data.get("TeamInfo").get("Name"), None, None)
                            parsernationalinfo(None, None,  doc.raw_data.get("TeamInfo").get("Area"))
                            parserarena(None, doc.raw_data.get("TeamInfo").get("Arena").get("Name"), None,
                                        doc.raw_data.get("TeamInfo").get("Arena").get("Address"),
                                        doc.raw_data.get("TeamInfo").get("Arena").get("Capacity"),
                                        doc.raw_data.get("TeamInfo").get("Arena").get("Opened"),
                                        doc.raw_data.get("TeamInfo").get("Arena").get("TicketPrice"))
                            leaguelist = list()
                            leaguelist.append(leagueid)
                            teambasic(leagueid=leaguelist, sport_type=1, name_info=nameinfo,
                                      league_area=0, logo=doc.raw_data.get("TeamInfo").get("Photo"),
                                      nationalinfo=nationalinfo,
                                      city_en="", city_zh=doc.raw_data.get("TeamInfo").get("City"),
                                      estableish_date=doc.raw_data.get("TeamInfo").get("EstablishDate"),
                                      join_date=doc.raw_data.get("TeamInfo").get("JoinUnitDate"),
                                      area_info=arena, coach_info=None,
                                      intro=doc.raw_data.get("TeamInfo").get("Intro"), update_user=None,
                                      referenceid=doc.raw_data.get("TeamInfo").get("Id"),
                                      create_time=datetime.now()).save()
                        else:
                            # CBA data
                            leaguefilter = Q(name_en="CBA")
                            leagueidList = set()
                            leagueid = league.findfirst(leaguefilter).id
                            leagueidList.add(leagueid)
                            parsernameinfo(doc.raw_data.get("TeamInfo").get("EnName"),
                                           doc.raw_data.get("TeamInfo").get("Name"), None,
                                           doc.raw_data.get("TeamInfo").get("ShortName"))
                            parsernationalinfo(None, None, doc.raw_data.get("TeamInfo").get("Area"))
                            parserarena(None, doc.raw_data.get("TeamInfo").get("Arena").get("Name"), None,
                                        doc.raw_data.get("TeamInfo").get("Arena").get("Address"),
                                        doc.raw_data.get("TeamInfo").get("Arena").get("Capacity"),
                                        doc.raw_data.get("TeamInfo").get("Arena").get("Opened"),
                                        doc.raw_data.get("TeamInfo").get("Arena").get("TicketPrice"))
                            leaguelist = list()
                            leaguelist.append(leagueid)
                            teambasic(leagueid=leaguelist, sport_type=1, name_info=nameinfo,
                                      league_area=0, logo=doc.raw_data.get("TeamInfo").get("Photo"),
                                      nationalinfo=nationalinfo,
                                      city_en="", city_zh=doc.raw_data.get("TeamInfo").get("City"),
                                      estableish_date=doc.raw_data.get("TeamInfo").get("EstablishDate"),
                                      join_date=doc.raw_data.get("TeamInfo").get("JoinUnitDate"),
                                      area_info=arena, coach_info=None,
                                      intro=doc.raw_data.get("TeamInfo").get("Intro"), update_user=None,
                                      referenceid=doc.raw_data.get("TeamInfo").get("Id"),
                                      create_time=datetime.now()).save()

def footballTeamparser():

    filter = Q(api_name="season_detail", source_id="7")
    data = raw_api_data.find(filter)
    teamdic = dict()
    for doc in data:
        leagueid = doc.raw_data.get("competition").get("id")
        # print(doc.raw_data.get("competition").get("name_zh"))
        # print(doc.raw_data.get("competition").get("name_en"))
        teamlist = doc.raw_data.get("teams")
        teamidlist = set()
        for team in teamlist:
            teamidlist.add(team.get("id"))
            teamdic[leagueid] = teamidlist

    for key in teamdic:
        print("key:", key)
        print("teamdic", teamdic[key])
        for teamid in teamdic[key]:
            print("teamid:", teamid)
            teamdetailfilter = Q(api_name="team_detail", source_id="7", raw_data__id=teamid)
            team = raw_api_data.findfirst(teamdetailfilter)
            teamlistfilter = Q(api_name="team_list", source_id="7", raw_data__id=teamid)
            teamlistdata = raw_api_data.findfirst(teamlistfilter)
            for doc in teamlistdata.raw_data:
                # print(doc)
                if doc.get("id") == teamid:
                    matcheventid = doc.get("matchevent_id")
                    print("matcheventid:", matcheventid)
            matcheventfilter = Q(api_name="match_even_list", source_id="7")
            matcheventslist = raw_api_data.findfirst(matcheventfilter)
            for doc in matcheventslist.raw_data.get("matchevents"):
                if doc.get("id") == matcheventid:
                    countryid = doc.get("country_id")
                    leaguename = doc.get("name_en")
                    print("leaguename:", leaguename)
                    leaguefilter = Q(name_en=leaguename)
                    leagueid = league.findfirst(leaguefilter).id
                    print("countryid:", countryid)
            for countrykey in matcheventslist.raw_data.get("countrys"):
                if countryid == matcheventslist.raw_data.get("countrys")[countrykey].get("id"):
                    data = matcheventslist.raw_data.get("countrys")[countrykey]
            if team is not None:
                print(team)
                parsernameinfo(team.raw_data.get("name_en"),
                               team.raw_data.get("name_zh"),
                               team.raw_data.get("short_name_en"),
                               team.raw_data.get("short_name_zh"))
                parsernationalinfo(data.get("logo"), data.get("name_en"), data.get("name_zh"))

                parserarena(None, team.raw_data.get("venue").get("name_zh"), None,
                            None,
                            team.raw_data.get("venue").get("capacity"),
                            None,
                            None)
                if team.raw_data.get("manager") is not None:
                    parsercoach(team.raw_data.get("manager").get("name_en"), team.raw_data.get("manager").get("name_zh"), team.raw_data.get("manager").get("logo"))

                leaguelist = list()
                leaguelist.append(leagueid)
                teambasic(leagueid=leaguelist, sport_type=2, name_info=nameinfo,
                          league_area=0, logo=team.raw_data.get("logo"),
                          nationalinfo=nationalinfo,
                          city_en="", city_zh="",
                          estableish_date="",
                          join_date="",
                          area_info=arena, coach_info=coach,
                          intro=None, update_user=None,
                          referenceid=teamid,
                          create_time=datetime.now()).save()

            else:
                print("teamid:", teamid, " is null")
        print("======================================")



# BasetballTeamparser()
footballTeamparser()
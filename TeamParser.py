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
coach = Coach()

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

                        teambasic(leagueidlist=leaguelist, sport_type=1, name_info=nameinfo,
                                  league_area=0, logo=doc.raw_data.get("TeamInfo").get("Photo"),
                                  nationalinfo=nationalinfo, isnational=0,
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
                            teambasic(leagueidlist=leaguelist, sport_type=1, name_info=nameinfo,
                                      league_area=0, logo=doc.raw_data.get("TeamInfo").get("Photo"),
                                      nationalinfo=nationalinfo, website = doc.raw_data.get("TeamInfo").get("Website"),
                                      city_en="", city_zh=doc.raw_data.get("TeamInfo").get("City"),isnational=1,
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
                            teambasic(leagueidlist=leaguelist, sport_type=1, name_info=nameinfo,
                                      league_area=0, logo=doc.raw_data.get("TeamInfo").get("Photo"),
                                      nationalinfo=nationalinfo,isnational=0,
                                      city_en="", city_zh=doc.raw_data.get("TeamInfo").get("City"),
                                      estableish_date=doc.raw_data.get("TeamInfo").get("EstablishDate"),
                                      join_date=doc.raw_data.get("TeamInfo").get("JoinUnitDate"),
                                      area_info=arena, coach_info=None,
                                      intro=doc.raw_data.get("TeamInfo").get("Intro"), update_user=None,
                                      referenceid=doc.raw_data.get("TeamInfo").get("Id"),
                                      create_time=datetime.now()).save()

def footballTeamparser():
    # get our league list
    leaguedfilter = Q(sport_type=2)
    referenceIdList = list()
    leaguelist = league.find(leaguedfilter)
    for doc in leaguelist:
        referenceIdList.append(doc.referenceid)

    # get each league team list from nami
    leagueteamdic = dict()
    leaguefilter = Q(api_name="season_list", source_id="7")
    lastleaguedata = raw_api_data.findlastOrderbyDate(leaguefilter)
    competitionlist = lastleaguedata.raw_data.get("competitions")
    # print("competitionlist", competitionlist)
    for leagueid in referenceIdList:
        print("leagueid", leagueid)
        for doc in competitionlist:
            # print("doc:", doc)
            print("doc id:", doc.get('id'), "leagueid:", leagueid)
            if doc.get('id') == int(leagueid):
                # print("doc id:", doc.get('id'), "leagueid:",  leagueid)
                if doc.get("seasons")[0] is None:
                    print(leagueid, "is not data on season_list")
                else:
                    seasonid = doc.get("seasons")[0].get('id')
                    # print("seasonid:", seasonid)
                    leaguefilter = Q(api_name="season_detail", query_parameter=str(seasonid))
                    seasondata = raw_api_data.findfirst(leaguefilter)

                    # print('seasondata:', seasondata)
                    teamlist = seasondata.raw_data.get("teams")
                    teamidlist = set()
                    for team in teamlist:
                        teamidlist.add(team.get("id"))
                        leagueteamdic[leagueid] = teamidlist

    # parser team basic data
    for key in leagueteamdic:
        print("key:", key)
        print("leaguedteamdic", leagueteamdic[key])
        # print("leaguedteamdic len", leagueteamdic[key].__len__())
        for teamid in leagueteamdic[key]:
            # print("teamid:", teamid)


            # get matcheventid
            teamlistfilter = Q(api_name="team_list", source_id="7")
            teamlistdata = raw_api_data.findfirst(teamlistfilter)
            for matchevendata in teamlistdata.raw_data:
                # print(matchevendata.get("id"), "key:", int(key))
                if int(matchevendata.get("id")) == int(teamid):
                    matcheventid = matchevendata.get("matchevent_id")
                    # print("matcheventid:", matcheventid)

             # use matcheventid to get country id
            matcheventfilter = Q(api_name="match_even_list", source_id="7")
            matcheventslist = raw_api_data.findfirst(matcheventfilter)
            for matchevent in matcheventslist.raw_data.get("matchevents"):
                if matchevent.get("id") == matcheventid:
                    countryid = matchevent.get("country_id")
                    #if country id = 0 is country league
                    if countryid != 0:
                        # get country detail
                        for countrykey in matcheventslist.raw_data.get("countrys"):
                            if countryid == matcheventslist.raw_data.get("countrys")[countrykey].get("id"):
                                countrydata = matcheventslist.raw_data.get("countrys")[countrykey]

            # get country detail
            for countrykey in matcheventslist.raw_data.get("countrys"):
                if countryid == matcheventslist.raw_data.get("countrys")[countrykey].get("id"):
                    countrydata = matcheventslist.raw_data.get("countrys")[countrykey]

            # get team details
            teamdetailfilter = Q(api_name="team_detail", source_id="7", raw_data__id=teamid)
            team = raw_api_data.findfirst(teamdetailfilter)

            #check rawdata nami team data is exist or not
            if team is not None:
                # print(team)
                checkfilter = Q(referenceid=teamid)
                existdata =teambasic.findfirst(checkfilter)
                print("existdata:", existdata)
                # check team data is exist on new db design
                if existdata is None:

                    #team info data
                    parsernameinfo(team.raw_data.get("name_en"),
                                   team.raw_data.get("name_zh"),
                                   team.raw_data.get("short_name_en"),
                                   team.raw_data.get("short_name_zh"))

                    #check this team is nation team or not
                    isnationflag =1
                    if countryid != 0:
                        parsernationalinfo(countrydata.get("logo"), countrydata.get("name_en"), countrydata.get("name_zh"))
                        isnationflag = 0

                    #check arena data
                    if team.raw_data.get("venue") is not None:
                        parserarena(None, team.raw_data.get("venue").get("name_zh"), None,
                                    None,
                                    team.raw_data.get("venue").get("capacity"),
                                    None,
                                    None)
                    # check coach data
                    if team.raw_data.get("manager") is not None:
                        parsercoach(team.raw_data.get("manager").get("name_en"), team.raw_data.get("manager").get("name_zh"), team.raw_data.get("manager").get("logo"))

                    # add league list
                    teamleaguelist = list()
                    for leaguedata in leaguelist:
                        if int(leaguedata.referenceid) == int(key):
                            teamleaguelist.append(leaguedata.id)
                            print("leaguedlist.id:", leaguedata.id)
                    teambasic(leagueidlist=teamleaguelist, sport_type=2, name_info=nameinfo,
                              league_area=0, logo=team.raw_data.get("logo"),website="",
                              nationalinfo=nationalinfo, isnational = isnationflag,
                              city_en="", city_zh="",
                              estableish_date="",
                              join_date="",
                              area_info=arena, coach_info=coach,
                              intro=None, update_user=None,
                              referenceid=teamid,
                              create_time=datetime.now()).save()
                else: # data already exist in db
                    # if db already have data on new db, get leaguelist check league is on the list, if is new league , add it and save
                    for leaguedata in leaguelist:
                        print("leaguedata.referenceid:", leaguedata.referenceid, " key")
                        if int(leaguedata.referenceid) == int(key):
                            if leaguedata.id not in existdata.leagueidlist:
                                existdata.leagueidlist.append(leaguedata.id)
                                existdata.save()

            else:
                #can't find data in nami
                print("teamid:", teamid, " is not find on nami")

        print("======================================")
# BasetballTeamparser()
footballTeamparser()
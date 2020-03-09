from model.league_category import league_category
from model.season_type import season_type
from model.raw_api_data import *
from datetime import datetime


def FootBallseasontypePaser():
    leaguelist = league_category.find(Q(sport_type=2))
    seasonlist = set()
    for league in leaguelist:
        print("id:", league.referenceid)
        filter = Q(api_name="season_list")
        lastleaguedata = raw_api_data.findfirst(filter)
        competitionlist = lastleaguedata.raw_data.get("competitions")
        for competition in competitionlist:
            # print("doc:", doc)
            # print("doc id:", doc.get('id'), "leagueid:", leagueid)
            if competition.get('id') == int(league.referenceid):
                # print("doc id:", competition.get('id'), "leagueid:",  league.referenceid)

                if competition.get("seasons")[0] is None:
                    print(league.referenceid, "is not data on season_list")
                    continue

                rawseasondetailfilter = Q(api_name="season_detail", query_parameter=str(competition.get("seasons")[0].get("id")))
                rawseasondetail = raw_api_data.findfirst(rawseasondetailfilter)
                if rawseasondetail is None:
                    print("id:", competition.get("seasons")[0].get("id"), " is rawseasondetail is null")
                    continue
                for i in range(len(rawseasondetail.raw_data.get("stages"))):
                    season_type(
                        leagueid = league.id,
                        sport_type = 2,
                        season_type = rawseasondetail.raw_data.get("stages")[i].get("mode"),
                        name_en = rawseasondetail.raw_data.get("stages")[i].get("name_en"),
                        name_zh = rawseasondetail.raw_data.get("stages")[i].get("name_zh"),
                        memo = None,
                        update_user = None,
                        update_time = None,
                        create_time = datetime.now()
                    ).save()

FootBallseasontypePaser()
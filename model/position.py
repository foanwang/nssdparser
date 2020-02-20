import os
from utils import config
from mongoengine import *
from mongoengine.queryset.visitor import Q
from datetime import datetime

os.chdir("..")
rootpath = os.getcwd()
config = config.configuration(rootpath)
try:
    connect(db=config.getconfig("DatawareHouse", "DBname"), username=config.getconfig("DatawareHouse", "Account"), password=config.getconfig("DatawareHouse", "Password"), host=config.getconfig("DatawareHouse", "FullURL"))
except ConnectionError:
    print("Could not connect to MongoDB", file=stderr)

class position(Document):
    sporttype = IntField()
    abbreviation =StringField(required=True, max_length=30)
    name = StringField(required=True, max_length=30)
    memo = StringField(required=False, max_length=50)

    def find(Q):
        return position.objects(Q)

    def findcount(Q):
        return position.objects(Q).count()

def savedataBySportType(sporttype, abbreviationlist, namelist):
    if len(abbreviationlist)!= len(namelist):
        print("two array is not same len!!!")
    date = position()
    for i in range(len(abbreviationlist)):
        date.sporttype = sporttype
        date.abbreviation = abbreviationlist[i]
        date.name = namelist[i]
        date.memo = None
        filter = Q(abbreviation=abbreviationlist[i], sporttype=sporttype)
        if position.findcount(filter) > 0:
            print("already have this data:"+abbreviationlist[i]+" "+namelist[i])
        else:
            print("save data:" + abbreviationlist[i] + " " + namelist[i])
            date.save()

alist = ["C", "SF", "PF", "SG", "PG", "F", "G"]
nameList=["中锋", "小前锋", "大前锋", "得分后卫", "组织后卫","前锋", "后卫"]
savedataBySportType(1, alist, nameList)
footballList = ["LW", "RW", "ST", "AM", "ML", "MC", "MR", "DM", "DL", "DC", "DR", "GK"]
footballNameList = ["左边锋", "右边锋", "前锋", "攻击型中", "左中场", "中路中场", "右中场", "防守型中", "左后卫", "中后卫", "右后卫", "守门员"]
savedataBySportType(2, footballList, footballNameList)



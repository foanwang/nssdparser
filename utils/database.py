from pymongo import MongoClient
import pymongo.errors

class MongoDatabase():

    def __init__(self, url, port, username, password, db):
        self.url = url
        self.username =username
        self.password = password
        self.port = port
        self.db = db
        self.connect()
        print("db init.....")

    def connect(self):
        try:
            mongourl = "mongodb://" +self.username + ":" + self.password + "@" + self.url + ":" + self.port+"/?authSource="+self.db
            print("db "+ mongourl +" connect.....")
            self.client = MongoClient(mongourl)
            print(self.client)
        except pymongo.errors.ConnectionFailure as e:
               print("connect fail")

    def getDB(self, client, dbname):
        db = client[dbname]
        print("getdb.....")
        return db

    def getCollection(self,db, collection):
        print("get collect...")
        collect = db[collection]
        return db[collection]

    def disconnect(self):
        print("db close")
        self.client.close()

    def disconnect(self):
        print("db close")
        self.client.close()

    def find(self, collect):
        db = self.client[self.db]
        collect = db[collect]
        return collect.find()

    def findone(self, collect):
        db = self.client[self.db]
        collect = db[collect]
        return collect.find_one()

    def insert(self, collect):
        db = self.client[self.db]
        collect = db[collect]
        return collect.find_one()

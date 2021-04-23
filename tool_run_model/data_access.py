import pymongo
from bson import ObjectId
from variable import MONGO_URI, MONGO_DB
class DataBase:
    MONGO_CLIENT = None
    AI_CONTEST = None
    def __init__(self):
        self.MONGO_URI = MONGO_URI
        self.MONGO_DB = MONGO_DB
    def connect(self):
        try:
            self.MONGO_CLIENT = pymongo.MongoClient(self.MONGO_URI)
            self.AI_CONTEST = self.MONGO_CLIENT[MONGO_DB]
            return self.AI_CONTEST
        except Exception as exc:
            print(exc)

    def disconnect(self):
        self.MONGO_CLIENT.close()

    def get_results(self):
        try:
            if self.AI_CONTEST == None:
                self.connect()
            query = self.AI_CONTEST["result"].find({
                "status" : "N"
            }).sort("time_submit", pymongo.ASCENDING)
            if query != None:
                return list(query)
            else:
                return None

        except Exception as exc:
            print("Error in get_results: %s" % str(exc))
            
    def update_result(self, dict_result):
        try:
            query = self.AI_CONTEST["result"].update_one({
                "_id" : ObjectId(dict_result["_id"])
            },{
                "$set" : dict_result
            }, upsert = True)
        except Exception as exc:
            print("Error in update_result: %s" % str(exc))
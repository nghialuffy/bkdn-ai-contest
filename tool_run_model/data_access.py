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

    def get_result(self):
        try:
            if self.AI_CONTEST == None:
                self.connect()
            query = self.AI_CONTEST["result"].find({
                "status" : "N"
            }).sort("time_submit", pymongo.ASCENDING).limit(1)
            return list(query)[0]
        except Exception as exc:
            if "'NoneType' object does not support item assignment" not in str(exc):
                print("Error in get_results: %s" % str(exc))
        return None
    def update_result(self, dict_result):
        try:
            query = self.AI_CONTEST["result"].update_one({
                "_id" : ObjectId(dict_result["_id"])
            },{
                "$set" : dict_result
            }, upsert = True)
        except Exception as exc:
            print("Error in update_result: %s" % str(exc))
    def get_language(self, language_id):
        try:
            query = self.AI_CONTEST["language"].find_one({
                "_id" : ObjectId(language_id)
            })
            if query != None and "name" in query:
                return query["name"].lower()
            else:
                return None
        except Exception as exc:
            print("Error in get_language: %s" % str(exc))

    def get_problem(self, problem_id):
        try:
            query = self.AI_CONTEST["problem"].find_one({
                "_id" : ObjectId(problem_id)
            },{
                "_id" : 1,
                "train_data" : 1,
                "test_data" : 1,
                "time_executed_limit" : 1
            })
            return query
        except Exception as exc:
            print("Error in get_language: %s" % str(exc))
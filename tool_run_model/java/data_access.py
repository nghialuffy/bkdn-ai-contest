import pymongo
from bson import ObjectId
from variable import MONGO_URI, MONGO_DB, LANGUAGE_NAME, MEDIA_PATH
import sys, os
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

    def get_language(self):
        try:
            query = self.AI_CONTEST["language"].find_one({
                "name" : LANGUAGE_NAME
            })
            if query != None and "name" in query:
                return str(query["_id"]).lower()
            else:
                return None
        except Exception as exc:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print("Error in get_language in line %s: %s" % (str(exc_tb.tb_lineno), str(exc)))

    def get_result(self, language_id):
        try:
            if self.AI_CONTEST == None:
                self.connect()
            query = self.AI_CONTEST["result"].find({
                "status" : "N",
                "language_id" : ObjectId(language_id)
            }).sort("time_submit", pymongo.ASCENDING).limit(1)
            return next(iter(list(query)), None)
        except Exception as exc:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print("Error in get_result in line %s: %s" % (str(exc_tb.tb_lineno), str(exc)))
        return None
        
    def update_result(self, dict_result):
        try:
            query = self.AI_CONTEST["result"].update_one({
                "_id" : ObjectId(dict_result["_id"])
            },{
                "$set" : dict_result
            }, upsert = True)
        except Exception as exc:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print("Error in update_result in line %s: %s" % (str(exc_tb.tb_lineno), str(exc)))

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
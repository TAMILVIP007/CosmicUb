from pymongo import MongoClient

from config import Vars


class MongoVars:
    def __init__(self):
        self.client = MongoClient(Vars.MONGO_URL)
        self.db = self.client.cosmicub
        self.keys = self.db.keys

    def set_key(self, key, value):
        if self.keys.find_one({"key": key}):
            return self.keys.update_one(
                {"key": key}, {"$set": {"value": value}}, upsert=True
            )
        return self.keys.insert_one({"key": key, "value": value})

    def get_key(self, key):
        try:
            return self.keys.find_one({"key": key})["value"]
        except:
            return None

    def del_key(self, key):
        return self.keys.delete_one({"key": key})

    def get_all_keys(self):
        return [x["key"] for x in self.keys.find()]

    def check_value(self, key, value):
        try:
            if self.keys.find_one({"key": key})["value"] == value:
                return True
            return False
        except TypeError:
            return False

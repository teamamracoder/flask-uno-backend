from db import mongo

class UserService():
    def get(self):
        users = mongo.db.users.find()
        return users
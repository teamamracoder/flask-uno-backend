from app.services import UserService
from flask import jsonify

class UserController:
    def __init__(self) -> None:
        self.user_service = UserService()

    def get(self):
        users = self.user_service.get()

        # list
        # data = [{**user, '_id': str(user['_id'])} for user in users]
        
        # dictionary
        data = {str(user['_id']) : {**user, '_id': str(user['_id'])} for user in users}

        return jsonify(data)
from flask import Blueprint
from app.controllers import UserController

user_bp = Blueprint("user",__name__)
user_controller = UserController()

@user_bp.route("/")
def users():
    return user_controller.get()

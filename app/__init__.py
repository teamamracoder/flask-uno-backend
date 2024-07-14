from flask import Flask
from .routes import register_blueprints
from db import mongo
from config import Config

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    mongo.init_app(app)

    register_blueprints(app)
    
    return app
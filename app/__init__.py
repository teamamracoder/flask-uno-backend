from flask import Flask
from .routes import register_blueprints
from db import mongo
from config import Config
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config.from_object(Config)
    mongo.init_app(app)

    register_blueprints(app)
    
    return app
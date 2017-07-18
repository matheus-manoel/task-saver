from flask import Flask, Blueprint, request
from flask_mongoengine import MongoEngine
from server.routes import create_api_routes
from visual.routes import create_visual_routes
from server import utils
from server import models


def create_app():
    app = Flask(__name__)
    app.register_blueprint(create_api_routes(Blueprint, request, utils, models))
    app.register_blueprint(create_visual_routes(Blueprint, request, models))

    app.config['MONGODB_SETTINGS'] = {
            'db': 'task-saver',
            'host': 'mongodb://localhost:27017',
            'connect': False
    }

    db = MongoEngine()
    db.init_app(app)

    return app

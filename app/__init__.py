from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import settings


def create_app():
    app = Flask(__name__)
    app.config.from_object(settings)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.name = app.config['APP_NAME']
    return app


app = create_app()
db = SQLAlchemy(app)


__import__('app.models')
__import__('app.api')

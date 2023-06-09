from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
def create_app():
    app = Flask(__name__, static_folder='./static')
    app.config.from_object(Config)
    db.init_app(app)
    migrate = Migrate(app, db)
    return app

app = create_app()
from app import routes, models
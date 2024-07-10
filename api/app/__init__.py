import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


sqlalchemy_options = {'pool_pre_ping': True, "pool_recycle": 600, "pool_size": 50, "max_overflow": 50}
db = SQLAlchemy(engine_options=sqlalchemy_options)


def create_app(config_name):
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config["ENV"] = os.getenv('FLASK_ENV')
    app.config["DEBUG"] = True

    db.init_app(app)

    return app
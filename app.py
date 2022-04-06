import os

from flask import Flask

from common.extensions import db, cors


# Directory
BASE_DIR = os.path.abspath(os.curdir)


# Init flask app
app = Flask(__name__)


# Init cors
cors.init_app(app)


# Init apps
import api
api.init_app(app)


# Init BD
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///{}/pingql.db'.format(BASE_DIR)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

with app.app_context():
    db.create_all()

"""
Extensions Third Apps
"""

from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


# Config BD
db = SQLAlchemy()


# Allow CORS
cors = CORS()

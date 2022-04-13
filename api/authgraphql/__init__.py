"""
Auth GrapQL API Module
"""

from . import mutations

from .routes import bp


def init_app(app):
   # Init API app

   app.register_blueprint(bp)

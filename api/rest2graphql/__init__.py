"""
GrapQL API Module
"""

#from . import resolvers # Uncomment when you use decorator in your resolvers
from .routes import bp


def init_app(app):
   # Init API app

   app.register_blueprint(bp)

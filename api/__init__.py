"""
API Modules
"""

from . import db2graphql, rest2graphql


def init_app(app):
    """
    Init modules
    """

    db2graphql.init_app(app)
    rest2graphql.init_app(app)

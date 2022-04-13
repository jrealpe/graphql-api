"""
API Modules
"""

from . import db2graphql, rest2graphql, authgraphql


def init_app(app):
    """
    Init modules
    """

    db2graphql.init_app(app)
    rest2graphql.init_app(app)
    authgraphql.init_app(app)

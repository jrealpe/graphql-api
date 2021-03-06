"""
Rest2GraphQL API routes
"""

from flask import Blueprint, request, jsonify, current_app as app

from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers
from ariadne.constants import PLAYGROUND_HTML

from .common import query, mutation
from .queries import (
    current_day_resolver,
    list_posts_resolver,
    retrieve_post_resolver
)
from .mutations import (
    create_post_resolver,
    update_post_resolver,
    delete_post_resolver
)


bp = Blueprint('rest2graphql', __name__, url_prefix='/api/rest/')


##############
# GraphQL API
##############

# Queries
query.set_field('currentDay', current_day_resolver)
query.set_field('getPost', retrieve_post_resolver)
query.set_field('listPosts', list_posts_resolver)

# Mutations
mutation.set_field('createPost', create_post_resolver)
mutation.set_field('updatePost', update_post_resolver)
mutation.set_field('deletePost', delete_post_resolver)

# Schema
type_defs = load_schema_from_path('api/rest2graphql/schema.graphql')
schema = make_executable_schema(
    type_defs, query, mutation
)

# APIs
@bp.route('/graphql', methods=['GET'])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@bp.route('/graphql', methods=['POST'])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code

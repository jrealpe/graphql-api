"""
DB2GraphQL API routes
"""

from flask import Blueprint, request, jsonify, current_app as app

from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML

from .queries import getPost_resolver, listPosts_resolver
from .mutations import create_post_resolver, update_post_resolver, \
    delete_post_resolver


bp = Blueprint('db2graphql', __name__, url_prefix='/api/db')


##############
# GraphQL API
##############

# Queries
query = ObjectType('Query')
query.set_field('getPost', getPost_resolver)
query.set_field('listPosts', listPosts_resolver)

# Mutations
mutation = ObjectType('Mutation')
mutation.set_field('createPost', create_post_resolver)
mutation.set_field('updatePost', update_post_resolver)
mutation.set_field('deletePost', delete_post_resolver)

# Schema
type_defs = load_schema_from_path('api/db2graphql/schema.graphql')
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
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


###########
# Rest API
###########

@bp.route('/welcome')
def hello():
    return 'Welcome dude!'


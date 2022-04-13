"""
Auth GraphQL API routes
"""

from flask import Blueprint, request, jsonify, current_app as app

from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML

from .common import mutation


bp = Blueprint('auth', __name__, url_prefix='/api/auth')


##############
# GraphQL API
##############

# Schema
type_defs = load_schema_from_path('api/authgraphql/schema.graphql')
schema = make_executable_schema(
    type_defs, mutation, snake_case_fallback_resolvers
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

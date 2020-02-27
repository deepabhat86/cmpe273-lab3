from flask import Flask, escape, request
from ariadne import QueryType, ObjectType, graphql_sync, make_executable_schema, MutationType, load_schema_from_path
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, request, jsonify
from ariadne import gql
import resolvers as r

type_defs = load_schema_from_path('schema.py')

query = QueryType()
query.set_field('students', r.get_student)
query.set_field('classes',r.get_class)

mutation = MutationType()
mutation.set_field('create_student', r.create_student)
mutation.set_field('create_class', r.create_class)
mutation.set_field('update_class', r.update_class)

# @query.field("hello")
# def resolve_hello(_, info):
#     request = info.context
#     user_agent = request.headers.get("User-Agent", "Guest")
#     return "Hello, %s!" % user_agent

schema = make_executable_schema(type_defs, query,mutation)


app = Flask(__name__)

@app.route("/graphql", methods=["GET"])
def graphql_playgroud():
    # On GET request serve GraphQL Playground
    # You don't need to provide Playground if you don't want to
    # but keep on mind this will not prohibit clients from
    # exploring your API using desktop GraphQL Playground app.
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    # GraphQL queries are always sent as POST
    data = request.get_json()

    # Note: Passing the request to the context is optional.
    # In Flask, the current request is always accessible as flask.request
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code



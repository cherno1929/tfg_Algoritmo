import flask
from Algorithm.Algorithm_Master import Algorithm_Master

api_algorithm_routes = flask.Blueprint("algorithm", __name__, url_prefix="/api/algorithms")

algorithm_master = Algorithm_Master()

@api_algorithm_routes.route('/ftlrp', methods=['POST'])
def solve_ftlrp():
    graph_data = flask.request.get_json()
    solution = algorithm_master.solve_ftlrp_problem(graph_data)
    return flask.jsonify(solution.to_dict())

@api_algorithm_routes.route('/ftlrp_checker', methods=['POST'])
def check_ftlrp():
    graph_data = flask.request.get_json()
    return flask.jsonify(algorithm_master.check_is_sol_client_req(graph_data))

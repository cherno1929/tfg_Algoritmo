import flask
from Algorithm.Algorithm_Master import Algorithm_Master

api_benchmark_routes = flask.Blueprint("benchmark", __name__, url_prefix="/api/benchmarks")

@api_benchmark_routes.route('/general', methods=['POST'])
def get_benckmark():
    algorithm_master = Algorithm_Master()
    graph_data = flask.request.get_json()
    results = algorithm_master.run_benchmark(graph_data)
    return flask.jsonify(results.to_dict())
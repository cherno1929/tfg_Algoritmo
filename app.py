import flask
from Algorithm.Algorithm_Master import Algorithm_Master

# Constrolls ftlrp algorithm
algorithm_master = Algorithm_Master()

app = flask.Flask(__name__)

@app.route('/')
def home():
    return flask.render_template("main_menu.html")

@app.route('/algorithms')
def algorithm_menu():
    return flask.render_template("ftlrp_menu.html")

@app.route('/benchmarks')
def get_benchmark_menu():
    return flask.render_template("benckmark.html")

#############################
# API
#############################

@app.route('/api/algorithms/ftlrp', methods=['POST'])
def solve_ftlrp():
    graph_data = flask.request.get_json()
    solution = algorithm_master.solve_ftlrp_problem(graph_data)
    return flask.jsonify(solution.to_dict())

@app.route('/api/benchmarks/general', methods=['POST'])
def get_benckmark():
    graph_data = flask.request.get_json()
    results = algorithm_master.run_benchmark(graph_data)
    return flask.jsonify(results.to_dict())


if __name__ == '__main__':
    app.run()
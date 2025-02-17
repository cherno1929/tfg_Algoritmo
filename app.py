import flask
from Algorithm.Algorithm_Master import Algorithm_Master
from Routers.Routes import routes
from Routers.API.AlgorithmAPI import api_algorithm_routes
from Routers.API.BenchmarkAPI import api_benchmark_routes

# Constrolls ftlrp algorithm
algorithm_master = Algorithm_Master()

app = flask.Flask(__name__)

# Give routes to server
app.register_blueprint(routes)
app.register_blueprint(api_algorithm_routes)
app.register_blueprint(api_benchmark_routes)

if __name__ == '__main__':
    app.run()
import flask

routes = flask.Blueprint("routes", __name__, url_prefix="/")

@routes.route('/')
def home():
    return flask.render_template("main_menu.html")

@routes.route('/algorithms')
def algorithm_menu():
    return flask.render_template("ftlrp_menu.html")

@routes.route('/benchmarks')
def get_benchmark_menu():
    return flask.render_template("benckmark.html")

@routes.route('/graph_creator')
def get_graph_creator_menu():
    return flask.render_template("graph_creator.html")

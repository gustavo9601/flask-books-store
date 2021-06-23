from flask import Flask, render_template

app = Flask(__name__)


def index():
    return render_template('index.html')


def page_not_found_404(error):
    print(f"Error :{error}")
    # The second param is the code error
    return render_template('errors/404.html'), 404


def init_app(config):
    # Init config from object
    app.config.from_object(config)

    # Routes
    app.add_url_rule('/', view_func=index, methods=['GET'])

    # Handler Errors
    app.register_error_handler(404, page_not_found_404)

    return app

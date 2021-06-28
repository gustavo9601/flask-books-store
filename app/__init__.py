from flask import Flask, render_template, request, redirect, url_for
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect()


def index():
    return render_template('index.html')


def login():
    if request.method == 'POST':
        print(request.form)
        # print(request.form['user'])
        # print(request.form['password'])
        return "Ok"
    else:
        return render_template('auth/login.html')


def page_not_found_404(error):
    print(f"Error :{error}")
    # The second param is the code error
    return render_template('errors/404.html'), 404


def init_app(config):
    # Init config from object
    app.config.from_object(config)

    # Init config CSRF
    csrf.init_app(app)

    # Routes
    app.add_url_rule('/', view_func=index, methods=['GET'])
    app.add_url_rule('/login', view_func=login, methods=['GET', 'POST'])

    # Handler Errors
    app.register_error_handler(404, page_not_found_404)

    return app

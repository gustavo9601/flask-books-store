from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_wtf.csrf import CSRFProtect
from flaskext.mysql import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_mail import Mail

from .models.BookModel import BookModel
from .models.PurchaseModel import PurchaseModel
from .models.UserModel import UserModel
from .models.entities.Book import Book
from .models.entities.Purchase import Purchase
from .models.entities.User import User
from .emails import confirm_buyed
from .const import *

app = Flask(__name__)
csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)
mail=Mail()


# Function own of flask login, to generate the session
@login_manager_app.user_loader
def load_user(id):
    return UserModel.get_user_by_id(db, id)


@login_required
def index():
    try:
        # current_user.is_authenticated // verification own of flask session
        if current_user.is_authenticated:
            # accede al typo de usuari seteado en el usuario alamcenado en la sesion
            if current_user.type_user_id.id == 1:
                books_sold = BookModel.list_books_sold(db)
                data = {
                    'title': 'Libros vendidos',
                    'libros_vendidos': books_sold
                }
            else:
                purchases = PurchaseModel.list_purchases_user(db, current_user)
                data = {
                    'title': 'Mis Compras',
                    'compras': purchases
                }
            return render_template('index.html', data=data)
        else:
            return redirect(url_for('login'))
    except Exception as ex:
        print(f"Error :{ex}")
        # raise Exception(ex)
        return render_template('errors/general.html', message=format(ex))


def login():
    if request.method == 'POST':
        user = User(None, request.form['user'], request.form['password'], None)
        user_logged = UserModel.login(db, user)
        if user_logged != None:
            # Send params to function own flask, to create a session with the user
            login_user(user_logged)
            flash(MENSAJE_BIENVENIDA, 'success')
            return redirect(url_for('index'))
        flash(LOGIN_CREDENCIALESINVALIDAS, 'warning')
        return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


def logout():
    # function own flask, to log out user from session
    logout_user()
    flash(LOGOUT, 'success')
    return redirect(url_for('login'))


@login_required
def list_books():
    try:
        books = BookModel.list_books(db)
        data = {
            'books': books,
            'titulo': 'Listado de libros'
        }
        return render_template('list_books.html', data=data)
    except Exception as ex:
        print(f"Error :{ex}")
        # raise Exception(ex)
        return render_template('errors/general.html', message=format(ex))


@login_required
def buy_book():
    # parseando a json el valor
    data_request = request.get_json()
    data = {}
    try:
        # book = Book(data_request['isbn'], None, None, None, None)
        book = BookModel.read_book(db, data_request['isbn'])
        print("book.isbn", book.isbn)
        purchase = Purchase(None, book, current_user)
        data['exito'] = PurchaseModel.register_purchase(db, purchase)
        confirm_buyed(app, mail, current_user, book)
    except Exception as ex:
        data['mensaje'] = ex
        data['exito'] = False
    # return json from a dictionary
    return jsonify(data)


def error_401(error):
    return redirect(url_for('login'))


def page_not_found_404(error):
    print(f"Error :{error}")
    # The second param is the code error
    return render_template('errors/404.html'), 404


def init_app(config):
    # Init config from object
    app.config.from_object(config)

    # Init config CSRF
    csrf.init_app(app)

    # Init mail service
    mail.init_app(app)

    # Routes
    app.add_url_rule('/', view_func=index, methods=['GET'])
    app.add_url_rule('/books', view_func=list_books, methods=['GET'])
    app.add_url_rule('/login', view_func=login, methods=['GET', 'POST'])
    app.add_url_rule('/buy_book', view_func=buy_book, methods=['POST'])
    app.add_url_rule('/logout', view_func=logout, methods=['GET'])

    # Handler Errors
    app.register_error_handler(404, page_not_found_404)
    app.register_error_handler(401, error_401)

    return app

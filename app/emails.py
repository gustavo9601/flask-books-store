from .models.entities.User import User
from .models.entities.Book import Book
from flask_mail import Message
from threading import Thread
from flask import current_app, render_template


def confirm_buyed(app, mail, user: User, book: Book):
    try:
        # current_app.config['MAIL_USERNAME'], // Accede a las variables de la clase de configuracion
        message = Message(
            'Confirmation buyed of Book',
            sender=current_app.config['MAIL_USERNAME'],
            recipients=['tavo9601@gmail.com']
        )

        message.html = render_template('emails/confimation_buyed.html', user=user, book=book)
        # Enviando el mensaje en el mismo hilo
        # mail.send(message)

        # Usando el mismo hilo
        treahd_email = Thread(target=send_message_aync, args=[app, mail, message])
        treahd_email.start() # iniciando el hilo

    except Exception as ex:
        print("Error sending email >>>", ex)
        raise Exception(ex)


def send_message_aync(app, mail, message):
    with app.app_context():
        # Enviando el mensaje en el mismo hilo
        mail.send(message)

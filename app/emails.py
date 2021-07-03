from .models.entities.User import User
from .models.entities.Book import Book
from flask_mail import Mail, Message

from flask import current_app, render_template


def confirm_buyed(mail, user: User, book: Book):
    try:
        # current_app.config['MAIL_USERNAME'], // Accede a las variables de la clase de configuracion
        message = Message(
            'Confirmation buyed of Book',
            sender=current_app.config['MAIL_USERNAME'],
            recipients=['tavo9601@gmail.com']
        )

        message.html = render_template('emails/confimation_buyed.html', user=user, book=book)
        # Enviando el mensaje
        mail.send(message)
    except Exception as ex:
        print("Error sending email >>>", ex)
        raise Exception(ex)

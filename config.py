from decouple import config as cf


class Config:
    SECRET_KEY = 'PruebaToken'


class DevelopmentConfig(Config):
    SECRET_KEY = 'PruebaToken'
    DEBUG = True
    MYSQL_DATABASE_HOST = 'localhost'
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = ''
    MYSQL_DATABASE_DB = 'flask_2'

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = cf('MAIL_USERNAME')
    MAIL_PASSWORD = cf('MAIL_PASSWORD')


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}

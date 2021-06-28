class Config:
    SECRET_KEY = 'PruebaToken'


class DevelopmentConfig(Config):
    SECRET_KEY = 'PruebaToken'
    DEBUG = True
    MYSQL_DATABASE_HOST = 'localhost'
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = ''
    MYSQL_DATABASE_DB='flask_2'


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}

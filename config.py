class Config:
    SECRET_KEY='PruebaToken'


class DevelopmentConfig(Config):
    SECRET_KEY='PruebaToken'
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}

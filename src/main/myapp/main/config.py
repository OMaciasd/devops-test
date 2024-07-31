class Config:
    DEBUG = False
    SECRET_KEY = 'P@2sW0r4'
    DATABASE_URI = 'sqlite:///database.db'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

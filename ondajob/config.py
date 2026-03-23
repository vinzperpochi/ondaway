import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "onda-job-dev-secret-key")
    # MySQL via phpMyAdmin — update credentials to match your setup
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "mysql+pymysql://root:@localhost/ondajob"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass

config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}

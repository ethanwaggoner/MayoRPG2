import os

from dotenv import load_dotenv


class Config(object):

    load_dotenv()

    basedir = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = os.getenv('SECRET_KEY', "hfuidshf7843tyf87t43f743ft34tf34tf3ffyf74f7y34yf")

    OAUTHLIB_RELAX_TOKEN_SCOPE = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'mayorpg.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECURITY_CONFIRMABLE = True


class ProductionConfig(Config):
    DEBUG = False

    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600



class DebugConfig(Config):
    DEBUG = True
    PROPAGATE_EXCEPTIONS = True
    SESSION_COOKIE_SECURE = False
    SESSION_COOKIE_SAMESITE = 'Lax'
    OAUTHLIB_INSECURE_TRANSPORT = True

config_dict = {
    'Production': ProductionConfig,
    'Debug'     : DebugConfig
}
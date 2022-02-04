"""
config.py
- settings for the flask application object
"""
from datetime import timedelta


class BaseConfig(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:G6kdi6pN0AFxo01x@35.240.11.106/db180'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # used for encryption and session management
    SECRET_KEY = '111mysecretkey111'
    SESSION_COOKIE_NAME = 'google-login-session'
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=5)


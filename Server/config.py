"""
config.py
- settings for the flask application object
"""


class BaseConfig(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///180.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # used for encryption and session management
    SECRET_KEY = '111mysecretkey111'
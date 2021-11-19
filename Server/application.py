"""
application.py
- creates a Flask app instance and registers the database object
"""

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.BaseConfig')

    from api.user import user
    app.register_blueprint(user)

    from api.trainee_volunteer import trainee
    app.register_blueprint(trainee)

    from api.group import group
    app.register_blueprint(group)

    from api.trainer import trainer
    app.register_blueprint(trainer)

    from api.training import training
    app.register_blueprint(training)

    from api.admin import admin
    app.register_blueprint(admin)

    return app

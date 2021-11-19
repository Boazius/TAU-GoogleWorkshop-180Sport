import flask
from flask import Blueprint, abort


admin = Blueprint('admin', __name__)


@admin.put('/disable_user')
def disable_user():
    return 1


@admin.get('/get_all_groups')
def get_all_groups():
    return 1


@admin.get('/get_all_trainers')
def get_all_trainers():
    return 1


@admin.get('/get_all_users')
def get_all_users():
    return 1


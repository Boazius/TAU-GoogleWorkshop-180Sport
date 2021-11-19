import flask
from flask import Blueprint, abort


group = Blueprint('group', __name__)


@group.post('/group')
def post_group():
    return 1


@group.put('/group')
def put_group():
    return 1


@group.delete('/group')
def delete_group():
    return 1


@group.get('/group')
def get_group():
    return 1


@group.put('/delete_user_from_group')
def delete_user_from_group():
    return 1


@group.put('/add_user_to_group')
def add_user_to_group():
    return 1


@group.get('/get_all_users_by_group')
def get_all_users_by_group():
    return 1


@group.get('/get_all_trainers_by_group')
def get_all_trainers_by_group():
    return 1


@group.get('/get_all_trainings_by_group')
def get_all_trainings_by_group():
    return 1

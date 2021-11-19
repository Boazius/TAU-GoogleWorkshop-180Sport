import flask
from flask import Blueprint, abort


training = Blueprint('training', __name__)


@training.post('/training')
def post_training_by_group_id():
    return 1


@training.put('/training')
def put_training():
    return 1


@training.delete('/training')
def delete_training():
    return 1


@training.get('/training')
def get_training():
    return 1


@training.get('/get_attendance_list_by_training')
def get_attendance_list_by_training():
    return 1

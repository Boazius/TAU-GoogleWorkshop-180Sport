import flask
from flask import Blueprint, abort


trainee = Blueprint('trainee_volunteer', __name__)


@trainee.post('/message')
def post_message():
    return 1


@trainee.put('/message')
def put_message():
    return 1


@trainee.delete('/message')
def delete_message():
    return 1


@trainee.get('/get_closest_training_by_user_id')
def get_closest_training_by_group_id():
    return 1


@trainee.put('/update_attendance')
def update_attendance():
    return 1


@trainee.get('/get_messages_by_user_and_training')
def get_messages_by_user_and_training():
    return 1



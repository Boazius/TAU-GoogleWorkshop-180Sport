import flask
from flask import Blueprint, abort


trainer = Blueprint('trainer', __name__)


@trainer.put('/attendance_list')
def update_attendance_list_per_training():
    return 1


@trainer.get('/groups_list')
def get_groups_by_trainer_id():
    return 1


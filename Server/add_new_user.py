from main import db
from models import User, User_type, Training, Group
from datetime import datetime, date
from flask import Blueprint, jsonify


def get_training_by_date(training_date, group_id):
    from main import db
    group_from_db = db.session.query(Group).filter_by(id=group_id).first()
    if not group_from_db:
        return jsonify({'success': False, 'message': 'No group found!'})
    date1 = training_date.split('-')
    print(date1)
    the_date = date(int(date1[0]), int(date1[1]), int(date1[2]))
    trainings_from_db = db.session.query(Training).all()
    chosen_training = None
    for training in trainings_from_db:
        if training.date == the_date:
            chosen_training = training
    print(chosen_training)

print(date.today())
get_training_by_date("2022-02-09", 3)
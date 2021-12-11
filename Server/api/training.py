import flask
from flask import Blueprint, abort,jsonify
from models import User, Group, Training, Attendance_options
from utils import token_required, login_required
import json
from sqlalchemy import func
training = Blueprint('training', __name__)


def id_in_group(group_ids, group_id):
    if group_ids == "":
        return False
    else:
        groups_list = group_ids.split(",")
    if str(group_id) in groups_list:
        return True
    return False

def list_intToString(lst):
    string_ints = [str(int) for int in lst]

    str_of_ints = ",".join(string_ints)
    return str_of_ints

@training.post('/training/by_group_id/')
@token_required
def post_training_by_group_id(current_user):
    from main import db
    from api.group import listToString
    if current_user.user_type in [3, 4]:
        return jsonify({"success": False,
                        "message": "User cannot create new trainig, unless it is admin/trainer"}), 401

    try:
        data = flask.request.json
        group_id = data['group_id']
        group_from_db = db.session.query(Group).filter_by(id=group_id).first()
        if not group_from_db:
            return jsonify({'success': False, 'message': 'No group found!'})
        users_from_db = db.session.query(User).all()
        list_of_trainers = []
        list_of_users = []
        for user in users_from_db:
            if user.user_type in [2] and id_in_group(user.group_ids, group_id):
                list_of_trainers.append(user.id)
            if user.user_type in [3, 4] and id_in_group(user.group_ids,group_id):
                list_of_users.append(user.id)
        notes_dict = dict((el, 0) for el in list_of_users)
        new_training = Training(group_id=group_id, day=group_from_db.day,
                                time=group_from_db.time,
                                meeting_place=group_from_db.meeting_place,
                                attendance_users=list_intToString(list_of_users),
                                is_happened=True,
                                trainers_id=list_intToString(list_of_trainers),
                                notes=json.dumps(notes_dict))
        db.session.add(new_training)
        training_id=db.session.query(func.max(Training.id)).scalar()
        training_string = group_from_db.trainings_list
        if training_string == "" or training_string is None:
            training_list = []
        else:
            training_list = training_string.split(",")
        training_list.append(str(training_id))
        group_from_db.trainings_list = listToString(training_list)
        db.session.commit()
        return jsonify({"success": True, "training": new_training.to_dict()})
    except:
            return jsonify(
            {"success": False, "message": "Something went wrong"}), 400

@training.put('/training/<training_id>/')
@token_required
def put_training(current_user, training_id):
    from main import db
    training_from_db = db.session.query(Training).filter_by(id=training_id).first()
    if not training_from_db:
        return jsonify({'success': False, 'message': 'No training found!'})
    if current_user.user_type in [3, 4]:
        return jsonify({"success": False,
                        "message": "User cannot update training details, unless it is admin/trainer"}), 401

    try:
        data = flask.request.json
        for key in data.keys():
            if key == 'day':
                training_from_db.day = data['day']
            if key == 'time':
                training_from_db.time = data['time']
            if key == 'meeting_place':
                training_from_db.meeting_place = data['meeting_place']
            if key == 'attendance_users':
                training_from_db.attendance_users = data['attendance_users']
            if key == 'is_happened':
                training_from_db.is_happened = data['is_happened']
            if key == 'trainers_id':
                training_from_db.trainers_id = data['trainers_id']
            if key == 'notes':
                training_from_db.notes = data['notes']
        db.session.commit()
        return jsonify({"success": True, "training": training_from_db.to_dict()})
    except:
        return jsonify(
            {"success": False, "message": "Something went wrong"}), 400


@training.delete('/training/<training_id>/')
@token_required
def delete_training(current_user,training_id):
    from main import db
    from api.group import listToString
    training_to_delete = db.session.query(Training).filter_by(id=training_id).first()
    if not training_to_delete:
        return jsonify({'success': False, 'message': 'No training found!'})
    if current_user.user_type in [3,4]:
        return jsonify({"success": False,
                        "message": "User cannot delete training, unless it is admin or trainer"}), 401
    group_id = int(training_to_delete.group_id)
    group_from_db = db.session.query(Group).filter_by(id=group_id).first()
    training_string = group_from_db.trainings_list
    if training_string == "":
        return jsonify({"success": False,
                        "message": "no training to delete in the group"}), 401
    else:
        training_list = training_string.split(",")
    if str(training_id) not in training_list:
        return jsonify({"success": False,
                        "message": "no training to delete in the group"}), 401
    training_list.remove(str(training_id))
    group_from_db.trainings_list = listToString(training_list)

    db.session.delete(training_to_delete)
    db.session.commit()
    return jsonify({"success": True,
                    "message": "Training: " + training_id + " at Group: " + str(group_id) + " was deleted successfully"}), 200


@training.get('/training/<training_id>/')
@token_required
def get_training(current_user,training_id):
    from main import db
    training_from_db = db.session.query(Training).filter_by(id=training_id).first()
    if not training_from_db:
        return jsonify({'success': False, 'message': 'No training found!'})

    return jsonify({'success': True, 'training': training_from_db.to_dict()})


@training.get('/training/get_attendance_list_by_training/<training_id>')
@token_required
def get_attendance_list_by_training(current_user,training_id):
    from main import db
    if current_user.user_type in [3, 4]:
        return jsonify({"success": False,
                        "message": "User cannot view attendance list per training, unless it is admin/trainer"}), 401
    try:
        training_from_db = db.session.query(Training).filter_by(id=training_id).first()
        if not training_from_db:
            return jsonify({'success': False, 'message': 'No training found!'})
        training_attendance = training_from_db.attendance_users
        if not training_attendance:
            return jsonify(
                {'success': False, 'message': 'No attendance for training found!'})
        return jsonify(
            {"success": True, "training_attendance": training_attendance})
    except:
        return jsonify(
            {"success": False, "message": "Something went wrong3"}), 400

@training.get('/training/get_messages_by_training/<training_id>/')
@token_required
def get_messages_by_user_and_training(current_user,training_id):
    from main import db
    if current_user.user_type in [3, 4]:
        return jsonify({"success": False,
                        "message": "User cannot view messages list per training, unless it is admin/trainer"}), 401
    training_from_db = db.session.query(Training).filter_by(id=training_id).first()
    return jsonify(
            {"success": True, "training_messages": training_from_db.notes})

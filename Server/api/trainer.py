import flask
from flask import Blueprint, jsonify
from models import User, Group, Training
from utils import token_required
import json
import datetime
from datetime import datetime, date

trainer = Blueprint('trainer', __name__)


def nearest(items, pivot):
    return min([i for i in items if i <= pivot], key=lambda x: abs(x - pivot))


@trainer.put('/trainer/update_attendance_list_per_training_per_user/<training_id>/')
@token_required
def update_attendance_list_per_training_per_user(current_user, training_id):
    from main import db
    if int(current_user.user_type) in [3, 4]:
        return jsonify({"success": False,
                        "message": "User cannot view attendance list per training, unless it is admin/trainer"}), 401
    try:
        data = flask.request.json
        user_id = data['user_id']
        user_from_db = db.session.query(User).filter_by(id=user_id).first()
        if not user_from_db:
            return jsonify({'success': False, 'message': 'No user found!'})
        training_from_db = db.session.query(Training).filter_by(id=training_id).first()
        if not training_from_db:
            return jsonify({'success': False, 'message': 'No training found!'})
        attendance = training_from_db.attendance_users
        if attendance is None:
            return jsonify({"success": False, "message": "attendance list is empty"}), 400
        else:
            attendance_dict = json.loads(attendance)
        if str(user_from_db.id) not in attendance_dict.keys():
            return jsonify({"success": False, "message": "user not in attendance training"}), 401
        attendance_dict[str(user_from_db.id)][0] = data['attendance']
        training_from_db.attendance_users = json.dumps(attendance_dict)
        db.session.commit()
        return jsonify({"success": True,
                        "message": "update attendance for training: " + training_id + " for user: " + str(
                            user_id) + " successfully"})
    except:
        return jsonify({"success": False, "message": "Something went wrong"}), 400



@trainer.get('/trainer/groups_list/<trainer_id>/')
@token_required
def get_groups_by_trainer_id(current_user, trainer_id):
    from main import db
    if int(current_user.user_type) in [3, 4]:
        return jsonify({"success": False,
                        "message": "User cannot view group list per training, unless it is admin/trainer"}), 401
    list_of_groups = []
    groups_from_db = db.session.query(Group).all()
    trainer_from_db = db.session.query(User).filter_by(id=trainer_id).first()
    if not trainer_from_db:
        return jsonify({'success': False, 'message': 'No trainer found!'})
    if trainer_from_db.user_type != 2:
        return jsonify({'success': False, 'message': 'No trainer found!'})

    trainer_groups = trainer_from_db.group_ids
    if trainer_groups is not None and trainer_groups != "":
        trainer_groups_list = trainer_groups.split(",")
        for group_id in trainer_groups_list:
            for group in groups_from_db:
                if int(group_id) == int(group.id):
                    list_of_groups.append(group.to_dict())
    return jsonify({"success": True, "trainer groups": list_of_groups}), 200


@trainer.get('/trainer/get_closest_training/<group_id>/')
@token_required
def get_closest_training(current_user, group_id):
    from main import db
    from api.trainee_volunteer import find_closest_date
    if int(current_user.user_type) not in [1, 2]:
        return jsonify({"success": False,
                        "message": "User cannot get training, unless it is the fit user or admin/trainer"}), 401
    today_date = date.today()
    b_d = datetime.strptime(str(today_date), "%Y-%m-%d")
    trainings = db.session.query(Training).filter_by(group_id=group_id).all()
    list_date = []
    for training in trainings:
        if not training:
            continue
            #return jsonify({"success": False, "message": "no training found"}), 400
        training_date = datetime.strptime(str(training.date), "%Y-%m-%d")
        if training_date >= b_d:
            list_date.append(training.date)
    if list_date is None or list_date == []:
        return jsonify({"success": False, "message": "no training found"}), 400
    the_date = min(list_date, key=find_closest_date)
    training_from_db = db.session.query(Training).filter_by(group_id=group_id, date=the_date).first()

    if not training_from_db:
        return jsonify({"success": False, "message": "no training found"}), 400

    return jsonify({"success": True, "training": training_from_db.to_dict()})


@trainer.get('/trainer/get_last_training/<group_id>/')
@token_required
def get_last_training(current_user, group_id):
    from main import db
    if int(current_user.user_type) in [3, 4]:
        return jsonify({"success": False,
                        "message": "User cannot get last training, unless it is the fit user or admin/trainer"}), 401
    today_date = date.today()
    b_d = datetime.strptime(str(today_date), "%Y-%m-%d")
    trainings = db.session.query(Training).filter_by(group_id=group_id).all()
    list_date = []
    for training in trainings:
        if not training:
            continue
            #return jsonify({"success": False, "message": "no training found"}), 400
        training_date = datetime.strptime(str(training.date), "%Y-%m-%d")
        if training_date < b_d:
            list_date.append(training.date)
    if list_date is None or list_date == []:
        return jsonify({"success": False, "message": "no training found"}), 400
    the_date = nearest(list_date, today_date)
    training_from_db = db.session.query(Training).filter_by(group_id=group_id, date=the_date).first()
    if not training_from_db:
        return jsonify({"success": False, "message": "no training found"}), 400
    return jsonify({"success": True, "training": training_from_db.to_dict()})


@trainer.post('/trainer/message/<user_id>/<training_id>/')
@token_required
def trainer_post_message(current_user,user_id,training_id):
    from main import db
    if int(current_user.user_type) != 1 and int(current_user.id) != int(user_id):
        return jsonify({"success": False, "message": "User cannot send message, unless it is the fit user"}), 401
    training_from_db = db.session.query(Training).filter_by(id=training_id).first()
    if not training_from_db:
        return jsonify({'success': False, 'message': 'No training found!'})

    try:
        data = flask.request.json
        message=data['message']
        trainee_id = data['trainee_id']
        trainer_notes=json.loads(training_from_db.trainer_notes)
        trainer_notes[trainee_id][1]=message
        trainer_notes[trainee_id][0]="0"
        training_from_db.trainer_notes=json.dumps(trainer_notes)
        db.session.commit()
        return jsonify({"success": True, "message": "message: " + message + " sent to user: " + trainee_id + " add to training successfully"})
    except:
        return jsonify({"success": False, "message": "Something went wrong"}), 400


@trainer.delete('/trainer/message/<user_id>/<training_id>/')
@token_required
def trainer_delete_message(current_user,user_id,training_id):
    from main import db
    if int(current_user.user_type) != 1 and int(current_user.id) != int(user_id):
        return jsonify({"success": False,
                        "message": "User cannot update message, unless it is the fit user"}), 401
    training_from_db = db.session.query(Training).filter_by(id=training_id).first()
    if not training_from_db:
        return jsonify({'success': False, 'message': 'No training found!'})
    try:
        data = flask.request.json
        trainee_id=data['trainee_id']
        trainer_notes = json.loads(training_from_db.trainer_notes)
        trainer_notes[trainee_id][1] = ""
        trainer_notes[trainee_id][0] = "0"
        training_from_db.trainer_notes = json.dumps(trainer_notes)
        db.session.commit()
        return jsonify({"success": True, "message": "message was deleted successfully"}), 200
    except:
        return jsonify({"success": False, "message": "Something went wrong"}), 400


@trainer.put('/trainer/update_attendance_list/<training_id>/')
@token_required
def update_attendance_list(current_user, training_id):
    from main import db
    if int(current_user.user_type) in [3, 4]:
        return jsonify({"success": False,
                        "message": "User cannot view attendance list per training, unless it is admin/trainer"}), 401
    try:
        data = flask.request.json
        training_from_db = db.session.query(Training).filter_by(id=training_id).first()
        if not training_from_db:
            return jsonify({'success': False, 'message': 'No training found!'})
        attendance = data["attendance_users"]
        if attendance is None:
            return jsonify({"success": False, "message": "attendance list is empty"}), 400
        training_from_db.attendance_users = json.dumps(attendance)
        db.session.commit()
        return jsonify({"success": True,
                        "message": "update attendance for training: " + training_id + " done successfully"})
    except:
        return jsonify({"success": False, "message": "Something went wrong"}), 400


@trainer.put('/trainer/update_notes/<training_id>/')
@token_required
def update_notes(current_user, training_id):
    from main import db
    if int(current_user.user_type) in [3, 4]:
        return jsonify({"success": False,
                        "message": "User cannot view notes list per training, unless it is admin/trainer"}), 401
    try:
        data = flask.request.json
        training_from_db = db.session.query(Training).filter_by(id=training_id).first()
        if not training_from_db:
            return jsonify({'success': False, 'message': 'No training found!'})
        notes = data["notes"]
        if notes is None:
            return jsonify({"success": False, "message": "notes list is empty"}), 400
        training_from_db.notes = json.dumps(notes)
        db.session.commit()
        return jsonify({"success": True,
                        "message": "update notes for training: " + training_id + " done successfully"})
    except:
        return jsonify({"success": False, "message": "Something went wrong"}), 400


@trainer.put('/trainer/update_notes_per_user/<training_id>/')
@token_required
def update_notes_per_user(current_user, training_id):
    from main import db
    if int(current_user.user_type) in [3, 4]:
        return jsonify({"success": False,
                        "message": "User cannot view notes list per training, unless it is admin/trainer"}), 401
    try:
        data = flask.request.json
        user_id = data['user_id']
        mark = data['mark']
        training_from_db = db.session.query(Training).filter_by(id=training_id).first()
        if not training_from_db:
            return jsonify({'success': False, 'message': 'No training found!'})
        notes = training_from_db.notes
        if notes is None:
            return jsonify({"success": False, "message": "notes list is empty"}), 400
        else:
            notes_dict = json.loads(notes)
        if str(user_id) not in notes_dict.keys():
            return jsonify({"success": False, "message": "user not in notes training"}), 401
        notes_dict[str(user_id)][0] = mark
        training_from_db.notes = json.dumps(notes_dict)
        db.session.commit()
        return jsonify({"success": True,
                        "message": "update notes for training: " + training_id + " for user: " + str(
                            user_id) + " successfully"})
    except:
        return jsonify({"success": False, "message": "Something went wrong"}), 400
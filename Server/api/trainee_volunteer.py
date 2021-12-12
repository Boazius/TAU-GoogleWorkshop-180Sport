import flask
import json
from flask import Blueprint, abort,jsonify
from models import User, Group, Training, Attendance_options
from utils import token_required, login_required

trainee = Blueprint('trainee_volunteer', __name__)


@trainee.post('/trainee/<user_id>/<training_id>/message')
@token_required
def post_message(current_user,user_id,training_id):
    from main import db
    from api.training import id_in_group
    if current_user.user_type != 1 and current_user.id != user_id:
        return jsonify({"success": False,
                        "message": "User cannot send message, unless it is the fit user"}), 401
    training_from_db = db.session.query(Training).filter_by(id=training_id).first()
    if not training_from_db:
        return jsonify({'success': False, 'message': 'No training found!'})
    if not id_in_group(current_user.group_ids, training_from_db.group_id): #user not in the group fit for training
        return jsonify({'success': False, 'message': 'user not in the group fit for training'})

    try:
        data = flask.request.json
        message=data['message']
        notes=json.loads(training_from_db.notes)
        notes[user_id]=message
        training_from_db.notes=json.dumps(notes)
        db.session.commit()
        return jsonify({"success": True, "message": "message: " + message + " from user: " + user_id + " add to training successfully"})
    except:
        return jsonify({"success": False, "message": "Something went wrong"}), 400

""""
כפילות - לא צריך
@trainee.put('/trainee/<user_id>/<training_id>/message')
@token_required
def put_message(current_user,user_id,training_id):
    from Server.main import db
    if current_user.user_id != user_id:
        return jsonify({"success": False,
                        "message": "User cannot update message, unless it is the fit user"}), 401
    training_from_db = db.session.query(Group).filter_by(id=training_id).first()
    if not training_from_db:
        return jsonify({'success': False, 'message': 'No training found!'})
    try:
        data = flask.request.json
        message = data['message']
        notes = json.loads(training_from_db.notes)
        notes['user_id'] = message
        db.session.commit()
        return jsonify({"success": True,
                        "message": "message: " + message + "from user: " + user_id + "add to training successfully"})
    except:
        return jsonify(
            {"success": False, "message": "Something went wrong"}), 400
"""


@trainee.delete('/trainee/<user_id>/<training_id>/message')
@token_required
def delete_message(current_user,user_id,training_id):
    from main import db
    if current_user.user_type != 1 and current_user.user_id != user_id:
        return jsonify({"success": False,
                        "message": "User cannot update message, unless it is the fit user"}), 401
    training_from_db = db.session.query(Training).filter_by(id=training_id).first()
    if not training_from_db:
        return jsonify({'success': False, 'message': 'No training found!'})
    notes = json.loads(training_from_db.notes)
    notes[user_id] = 0
    training_from_db.notes = json.dumps(notes)
    db.session.commit()
    return jsonify({"success": True,
                    "message": "message was deleted successfully"}), 200

"""""
@trainee.get('/trainee/<user_id>/get_closest_training_by_user_id')
@token_required
def get_closest_training_by_group_id(current_user,user_id,group_id):
    from Server.main import db
    group_from_db = db.session.query(Group).filter_by(id=group_id).first()
    trainings=group_from_db.trainings_list
    

"""""


@trainee.get('/trainee/<user_id>/get_closest_training_by_user_id/<training_id>/')
@token_required
def get_closest_training_by_group_id(current_user, user_id, training_id):
    from main import db
    training_from_db = db.session.query(Training).filter_by(id=training_id).first()
    if current_user.user_type in [3,4] and current_user.user_id != user_id:
        return jsonify({"success": False,
                    "message": "User cannot get training, unless it is the fit user or admin/trainer"}), 401
    if training_from_db.group_id not in current_user.group_ids:
        return jsonify({"success": False,
                        "message": "User cannot get training, unless the user is in the fit group"}), 401
    return jsonify({"success": True,
                    "message": training_from_db.to_dict()}), 401


@trainee.put('/trainee/<user_id>/update_attendance')
@token_required
def update_attendance(current_user, user_id):
    from main import db
    if current_user.user_type not in [1, 2] and current_user.user_id != user_id:
        return jsonify({"success": False,
                        "message": "User cannot update message, unless it is the fit user or admin/trainer"}), 401

    user_from_db = db.session.query(User).filter_by(id=user_id).first()
    if not user_from_db:
        return jsonify({"success": False,"message": "no user found"}), 401
    try:
        data = flask.request.json
        user_from_db.attendance = data['attendance']
        db.session.commit()
        return jsonify({"success": True, "user": "user update is attendance to:" + data['attendance'] })
    except:
        return jsonify({"success": False, "message": "Something went wrong"}), 400





import flask
from flask import Blueprint, abort, jsonify
from models import User, Group, Training, Attendance_options
from utils import token_required, login_required

trainer = Blueprint('trainer', __name__)


@trainer.put('/trainer/update_attendance_list_per_training_per_user/<training_id>/')
@token_required
def update_attendance_list_per_training_per_user(current_user, training_id):
    from main import db
    from api.group import listToString

    if current_user.user_type in [3, 4]:
        return jsonify({"success": False,
                        "message": "User cannot view attendance list per training, unless it is admin/trainer"}), 401

    try:
        data = flask.request.json
        user_id = int(data['user_id'])
        user_from_db = db.session.query(User).filter_by(id=user_id).first()
        if not user_from_db:
            return jsonify({'success': False, 'message': 'No user found!'})
        training_from_db = db.session.query(Training).filter_by(
            id=training_id).first()
        if not training_from_db:
            return jsonify({'success': False, 'message': 'No training found!'})
        attendance_string = training_from_db.attendance_users
        if attendance_string == "":
            return jsonify({"success": False,
                            "message": "attendance list is empty"}), 401
        else:
            attendance_list = attendance_string.split(",")

        if str(user_id) not in attendance_list:
            return jsonify({"success": False,
                            "message": "user not in attendance training"}), 401
        attendance_list.remove(str(user_id))
        training_from_db.attendance_users = listToString(attendance_list)
        user_from_db.attendance = data['attendance']
        db.session.commit()
        return jsonify({"success": True,
                        "message": "update attendance for training: " + training_id + " for user: " + str(
                            user_id) + " successfully"})
    except:
        return jsonify(
            {"success": False, "message": "Something went wrong"}), 400


@trainer.get('/trainer/groups_list/<trainer_id>/')
@token_required
def get_groups_by_trainer_id(current_user, trainer_id):
    from main import db
    if current_user.user_type in [3, 4]:
        return jsonify({"success": False,
                        "message": "User cannot view attendance list per training, unless it is admin/trainer"}), 401

    trainer_from_db = db.session.query(User).filter_by(id=trainer_id).first()
    if not trainer_from_db:
        return jsonify({'success': False, 'message': 'No trainer found!'})
    if trainer_from_db.user_type != 2:
        return jsonify({'success': False, 'message': 'No trainer found!'})

    trainer_groups = trainer_from_db.group_ids
    return jsonify({"success": True, "trainer groups": trainer_groups}), 401

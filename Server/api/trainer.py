import flask
from flask import Blueprint, abort,jsonify
from Server.models import User, Group, Training, Attendance_options
from Server.utils import token_required, login_required
trainer = Blueprint('trainer', __name__)



@trainer.put('/trainer/update_attendance_list_per_training_per_user/<training_id>/')
@token_required
def update_attendance_list_per_training_per_user(current_user, training_id):
    from Server.main import db
    from training import get_attendance_list_by_training

    if current_user.user_type in [3, 4]:
        return jsonify({"success": False,
                        "message": "User cannot view attendance list per training, unless it is admin/trainer"}), 401

    training_attendance = get_attendance_list_by_training(current_user,training_id)
    try:
        data = flask.request.json
        user_id = int(data['user_id'])
        user_from_db = db.session.query(User).filter_by(id=user_id).first()
        if not user_from_db:
            return jsonify({'success': False, 'message': 'No user found!'})
        training_attendance.user_from_db.id=data['name']
        db.session.commit()
        return jsonify({"success": True, "update attendance for training": training_id})
    except:
        return jsonify({"success": False, "message": "Something went wrong"}), 400


@trainer.get('/trainer/groups_list/<trainer_id>/')
@token_required
def get_groups_by_trainer_id(current_user,trainer_id):
    from Server.main import db
    if current_user.user_type in [3, 4]:
        return jsonify({"success": False,
                        "message": "User cannot view attendance list per training, unless it is admin/trainer"}), 401

    trainer_from_db = db.session.query(User).filter_by(id=trainer_id).first()
    if not trainer_from_db:
        return jsonify({'success': False, 'message': 'No trainer found!'})

    trainer_groups=trainer_from_db.group_ids
    return jsonify({"success": True,"trainer groups": trainer_groups}), 401



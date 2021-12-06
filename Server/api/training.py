import flask
from flask import Blueprint, abort,jsonify
from Server.models import User, Group, Training, Attendance_options
from Server.utils import token_required, login_required
training = Blueprint('training', __name__)


@training.post('/training/<group_id>/')
@token_required
def post_training_by_group_id(current_user,group_id):
    from group import get_all_trainers_by_group, get_all_users_by_group
    from Server.main import db
    if current_user.user_type in [3, 4]:
        return jsonify({"success": False,
                        "message": "User cannot create new trainig, unless it is admin/trainer"}), 401
    try:
        group_from_db = db.session.query(Group).filter_by(id=group_id).first()
        if not group_from_db:
            return jsonify({'success': False, 'message': 'No user found!'})
        trainers= get_all_trainers_by_group(current_user, group_id)
        users=get_all_users_by_group((current_user, group_id))
        users_id=[]
        for user in users:
            users_id.append(user.id)
        notes_dict=dict((el, 0) for el in users_id)
        new_training = Training(group_id=group_id, day=group_from_db.day,
                                time=group_from_db.time,
                                meeting_place=group_from_db.meeting_place,
                                attendance_users=users,
                                is_happened=True,
                                trainers_id=trainers,
                                notes=notes_dict)
        db.session.add(new_training)
        db.session.commit()
        return jsonify({"success": True, "training": new_training.to_dict()})
    except:
            return jsonify(
            {"success": False, "message": "Something went wrong"}), 400

@training.put('/training/<training_id>/')
@token_required
def put_training(current_user, training_id):
    from Server.main import db
    training_from_db = db.session.query(Training).filter_by(id=training_id).first()
    if not training_from_db:
        return jsonify({'success': False, 'message': 'No group found!'})
    if current_user.user_type in [3, 4]:
        return jsonify({"success": False,
                        "message": "User cannot update group details, unless it is admin/trainer"}), 401
    data = flask.request.json
    try:
        for key in data.keys():
            if key == 'day':
                training_from_db.day = data['day']
            if key == 'time':
                training_from_db.time = data['time']
            if key == 'meeting_place':
                training_from_db.meeting_place = data['meeting_place']
            if key == 'attendance_users':
                training_from_db.trainers_list = data['attendance_users']
            if key == 'is_happened':
                training_from_db.trainees_list = data['is_happened']
            if key == 'trainers_id':
                training_from_db.volunteers_list = data['trainers_id']
            if key == 'notes':
                training_from_db.trainings_list = data['notes']
        db.session.commit()
        return jsonify({"success": True, "training": training_from_db.to_dict()})
    except:
        return jsonify(
            {"success": False, "message": "Something went wrong"}), 400


@training.delete('/training/<training_id>/')
@token_required
def delete_training(current_user,training_id):
    from Server.main import db
    training_to_delete = db.session.query(Training).filter_by(id=training_id).first()
    group_id=training_to_delete.group_id
    if not training_to_delete:
        return jsonify({'success': False, 'message': 'No training found!'})
    if current_user.user_type in [3,4]:
        return jsonify({"success": False,
                        "message": "User cannot delete groups, unless it is admin or trainer"}), 401
    db.session.delete(training_to_delete)
    db.session.commit()
    return jsonify({"success": True,
                    "message": "Training: " + training_id + "at Group: " + group_id + "was deleted successfully"}), 200


@training.get('/training/<training_id>/')
@token_required
def get_training(current_user,training_id):
    from Server.main import db
    training_from_db = db.session.query(Training).filter_by(id=training_id).first()
    if not training_from_db:
        return jsonify({'success': False, 'message': 'No group training!'})

    return jsonify({'success': True, 'user': training_from_db.to_dict()})


@training.get('/training/get_attendance_list_by_training/<training_id>')
@token_required
def get_attendance_list_by_training(current_user,training_id):
    from Server.main import db
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
                {'success': False, 'message': 'No attendance training found!'})
        return jsonify(
            {"success": True, "training_attendance": training_attendance})
    except:
        return jsonify(
            {"success": False, "message": "Something went wrong3"}), 400

@training.get('/training/get_messages_by_training')
@token_required
def get_messages_by_user_and_training(current_user,training_id):
    from Server.main import db
    if current_user.user_type in [3, 4]:
        return jsonify({"success": False,
                        "message": "User cannot view messages list per training, unless it is admin/trainer"}), 401
    training_from_db = db.session.query(Training).filter_by(id=training_id).first()
    return jsonify(
            {"success": True, "training_messages": training_from_db.notes})

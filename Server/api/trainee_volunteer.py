
import flask
import json
from flask import Blueprint, abort, jsonify, Response
from models import User, Group, Training, Attendance_options
from utils import token_required, login_required
import datetime
from datetime import  datetime, timedelta,date

trainee = Blueprint('trainee_volunteer', __name__)

def find_closest_date(x):
    today_date=date.today()
    b_d = datetime.strptime(str(today_date), "%Y-%m-%d")
    d = datetime.strptime(str(x), "%Y-%m-%d")
    delta = d - b_d if d > b_d else timedelta.max
    return delta

@trainee.post('/trainee/message/<user_id>/<training_id>/')
@token_required
def post_message(current_user,user_id,training_id):
    from main import db
    from api.training import id_in_group

    if int(current_user.user_type) != 1 and int(current_user.id) != int(user_id):
        return jsonify({"success": False,
                        "message": "User cannot send message, unless it is the fit user"}), 401
    training_from_db = db.session.query(Training).filter_by(id=training_id).first()
    if not training_from_db:
        return jsonify({'success': False, 'message': 'No training found!'})
    if int(current_user.user_type) != 1 and not id_in_group(current_user.group_ids, training_from_db.group_id): #user not in the group fit for training
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


@trainee.delete('/trainee/message/<user_id>/<training_id>/')
@token_required
def delete_message(current_user,user_id,training_id):
    from main import db
    if int(current_user.user_type) != 1 and int(current_user.id) != int(user_id):
        return jsonify({"success": False,
                        "message": "User cannot update message, unless it is the fit user"}), 401
    training_from_db = db.session.query(Training).filter_by(id=training_id).first()
    if not training_from_db:
        return jsonify({'success': False, 'message': 'No training found!'})
    notes = json.loads(training_from_db.notes)
    notes[user_id] = ""
    training_from_db.notes = json.dumps(notes)
    db.session.commit()
    return jsonify({"success": True,
                    "message": "message was deleted successfully"}), 200

@trainee.get('/trainee/get_message_from_trainer/<user_id>/<training_id>/')
@token_required
def get_message_from_trainer(current_user,user_id,training_id):
    from main import db
    if int(current_user.user_type) not in [1,2] and int(current_user.id) != int(user_id):
        return jsonify({"success": False, "message": "User cannot send message, unless it is the fit user"}), 401
    training_from_db = db.session.query(Training).filter_by(id=training_id).first()
    if not training_from_db:
        return jsonify({'success': False, 'message': 'No training found!'})
    trainer_notes = json.loads(training_from_db.trainer_notes)
    if not trainer_notes:
        return jsonify({'success': False, 'message': 'No notes from trainer for training found!'})
    message=trainer_notes[str(user_id)]
    return jsonify( {"success": True, "messages":message})


@trainee.get('/trainee/get_closest_training/<user_id>/')
@token_required
def get_closest_training(current_user,user_id):
    from main import db
    from api.training import id_in_group

    if int(current_user.user_type) in [3,4] and int(current_user.id) != int(user_id):
        return jsonify({"success": False,
                    "message": "User cannot get training, unless it is the fit user or admin/trainer"}), 401
    user_from_db = db.session.query(User).filter_by(id=user_id).first()
    if not user_from_db:
        return jsonify({"success": False,"message": "no user found"}), 400
    today_date=date.today()
    b_d = datetime.strptime(str(today_date), "%Y-%m-%d")
    dict_training_date={}
    user_groups = user_from_db.group_ids
    if user_groups != "" and user_groups is not None:
        user_groups_list = user_groups.split(",")
    for group_id in user_groups_list:
        trainings = db.session.query(Training).filter_by(group_id=int(group_id)).all()
        list_date=[]
        for training in trainings:
            if not training:
                return jsonify({"success": False, "message": "no training found"}), 400
            training_date = datetime.strptime(str(training.date), "%Y-%m-%d")
            if training_date>b_d:
                list_date.append(training.date)
        if list_date is None or list_date==[]:
            return jsonify({"success": False, "message": "no training found"}), 400
        the_date=min(list_date, key=find_closest_date)
        training_from_db =db.session.query(Training).filter_by(group_id=group_id,date=the_date).first()
        if not training_from_db:
            return jsonify({"success": False, "message": "no training found"}), 400
        if int(current_user.user_type) != 1 and not id_in_group(current_user.group_ids,training_from_db.group_id):  # user not in the group fit for training
            return jsonify({"success": False,
                            "message": "User cannot get training, unless the user is in the fit group"}), 401
        date_value=datetime.strptime(str(training_from_db.date),"%Y-%m-%d")
        dict_training_date[training_from_db.id]=date_value

    if dict_training_date == {}:
        return jsonify({"success": False, "message": "no training found"}), 400
    the_id= min(dict_training_date,key=dict_training_date.get) #get the key corresponding to the minimum value within a dictionary
    the_training = db.session.query(Training).filter_by(id=the_id).first()
    if not the_training:
        return jsonify({"success": False, "message": "no training found"}), 400

    return jsonify({'success': True, 'training': the_training.to_dict()})


@trainee.get('/trainee/get_closest_training_by_training_id/<user_id>/<training_id>/')
@token_required
def get_closest_training_by_training_id(current_user, user_id, training_id):
    from main import db
    training_from_db = db.session.query(Training).filter_by(id=training_id).first()
    if not training_from_db:
        return jsonify({"success": False,"message": "no training found"}), 401
    if current_user.user_type in [3,4] and current_user.id != user_id:
        return jsonify({"success": False,
                    "message": "User cannot get training, unless it is the fit user or admin/trainer"}), 400
    if training_from_db.group_id not in current_user.group_ids:
        return jsonify({"success": False,
                        "message": "User cannot get training, unless the user is in the fit group"}), 401
    return jsonify({"success": True,
                    "message": training_from_db.to_dict()})


@trainee.put('/trainee/update_attendance/<user_id>/')
@token_required
def update_attendance(current_user, user_id):
    from main import db
    if int(current_user.user_type) not in [1, 2] and int(current_user.id) != int(user_id):
        return jsonify({"success": False,
                        "message": "User cannot update message, unless it is the fit user or admin/trainer"}), 401

    user_from_db = db.session.query(User).filter_by(id=user_id).first()
    if not user_from_db:
        return jsonify({"success": False,"message": "no user found"}), 400

    try:
        data = flask.request.json
        user_from_db.attendance = data['attendance']
        training = get_closest_training(user_id).json["training"]
        if not training:
            return jsonify({"success": False, "message": "no training found"}), 400
        attendance = training["attendance_users"]
        training_id = training["id"]
        if attendance is None:
            return jsonify({"success": False, "message": "attendance list is empty"}), 400
        a = str([str(user_id), str(user_from_db.full_name)])
        if a not in attendance.keys():
            return jsonify({"success": False, "message": "user not in attendance training"}), 400
        attendance[a] = str(data['attendance'])
        training_from_db = db.session.query(Training).filter_by(id=int(training_id)).first()
        if not training_from_db:
            return jsonify({"success": False, "message": "no training found"}), 400
        training_from_db.attendance_users = json.dumps(attendance)
        db.session.commit()
        return jsonify({"success": True, "user": "user update is attendance to:" + str(data['attendance'])})
    except:
        return jsonify({"success": False, "message": "Something went wrong"}), 400

import datetime
import flask
import jwt
from flask import Blueprint, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

from Server.models import User
from Server.utils import token_required

user = Blueprint('user', __name__)


@user.post('/login')
def login():
    from Server.main import db, app
    auth = flask.request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({"success": False, "message": "Authentication credentials were not supplied"}), 400
    user_from_db = db.session.query(User).filter_by(email=auth.username).first()
    if not user_from_db:
        return jsonify({"success": False, "message": "User does not exist with current email"}), 400
    if check_password_hash(user_from_db.password, auth.password):
        token = jwt.encode(
            {'id': user_from_db.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30), 'email':
                user_from_db.email}, app.config['SECRET_KEY'], algorithm="HS256")
        return jsonify({'success': True, 'token': token, 'user': user_from_db.to_dict()})
    return jsonify({'success': False, "message": "Incorrect password"}), 400


@user.post('/signup')
def signup():
    from Server.main import db
    try:
        data = flask.request.json
        user_exists = db.session.query(User).filter_by(email=data['email']).first()
        if user_exists:
            return jsonify({'success': False, 'message': 'User with current email is already exists'}), 400
        hashed_password = generate_password_hash(data['password'], method='sha256')
        new_user = User(user_type=int(data['user_type']), email=data['email'], full_name=data['full_name'],
                        phone_number=str(data['phone_number']), active_or_not=True, attendance=int(1),
                        password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"success": True, "user": new_user.to_dict()})
    except:
        return jsonify({"success": False, "message": "Something went wrong"}), 400


@user.post('/logout')
def logout():
    # !!!!!!!THINK ABOUT WHAT DOING HERE!!!!! #####
    return 1


@user.put('/user/<user_id>')
@token_required
def update_user_by_id(current_user, user_id):
    from Server.main import db
    if current_user.user_type in [3, 4] and current_user.id != user_id:
        return jsonify({"success": False,
                        "message": "User cannot update different user details, unless it is admin/trainer"}), 401
    data = flask.request.json
    user_from_db = db.session.query(User).filter_by(id=user_id).first()

    for key in data.keys():
        if key == 'email':
            user_exists = db.session.query(User).filter_by(email=data['email']).first()
            if user_exists:
                return jsonify({'success': False, 'message': 'User with current email is already exists'}), 400
            user_from_db.email = data['email']
        if key == 'password':
            hashed_password = generate_password_hash(data['password'], method='sha256')
            user_from_db.password = hashed_password
        if key == 'full_name':
            user_from_db.full_name = data['full_name']
        if key == 'phone_number':
            user_from_db.phone_number = str(data['phone_number'])
        if key == 'attendance':
            user_from_db.attendance = data['attendance']
    db.session.commit()
    return jsonify({"success": True, "user": user_from_db.to_dict()})
    # except:
      # return jsonify({"success": False, "message": "Something went wrong"}), 400
    return 1


@user.delete('/user')
def delete_user():
    return 1


@user.get('/user/<user_id>')
@token_required
def get_user(current_user, user_id):
    from Server.main import db
    if current_user.user_type in [3, 4] and current_user.id != user_id:
        return jsonify({"success": False,
                        "message": "User cannot view different user details, unless it is admin/trainer"}), 401
    user_from_db = db.session.query(User).filter_by(id=user_id).first()
    if not user_from_db:
        return jsonify({'success': False, 'message': 'No user found!'})
    return jsonify({'success': True, 'user': user_from_db.to_dict()})

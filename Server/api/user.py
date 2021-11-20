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
        return jsonify({"message": "Authentication credentials were not supplied"}), 400
    user = db.session.query(User).filter_by(full_name=auth.username).first()
    if not user:
        return jsonify({"message": "User does not exist"}), 400
    if check_password_hash(user.password, auth.password):
        token = jwt.encode(
            {'id': user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
            app.config['SECRET_KEY'], algorithm="HS256")
        # return jsonify({'token': jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])})
        return jsonify({'token': token})
    return jsonify({"message": "Incorrect password"}), 400

    # json_data = flask.request.json
    # email = json_data['email']
    # password = json_data['password']
    # remember = json_data['remember']
    # from main import db
    # user = db.session.query(User).filter_by(email=email).first()
    # if not user:
    # return str("User does not exist")
    # login_user(user, remember=remember)
    # return jsonify(user.to_dict())


@user.post('/signup')
def signup():
    from Server.main import db
    try:
        data = flask.request.json
        user_exists = db.session.query(User).filter_by(email=data['email']).first()
        if user_exists:
            return jsonify({'success':False, 'message': 'User with current email is already exists'})
        hashed_password = generate_password_hash(data['password'], method='sha256')
        new_user = User(user_type=int(data['user_type']), email=data['email'], full_name=data['full_name'],
                        phone_number=str(data['phone_number']), active_or_not=True, attendance=int(1),
                        password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"success": True, "user": new_user.to_dict()})
    except:
        return jsonify({"success": False, "message": "Something went wrong"})


@user.post('/logout')
def logout():
    return 1


@user.put('/user')
def update_user():
    return 1


@user.delete('/user')
def delete_user():
    return 1


@user.get('/user/<user_id>')
@token_required
def get_user(current_user, user_id):
    if current_user.user_type == 3 or current_user.user_type == 4:
        if current_user.id != user_id:
            return jsonify({'message': 'Unauthorized'}), 401
    from main import db
    user = db.session.query(User).filter_by(id=user_id).first()
    if not user:
        return jsonify({'message': 'No user found!'})
    return jsonify({'user': user.to_dict()})

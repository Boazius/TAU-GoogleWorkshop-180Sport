import datetime
import flask
import jwt
from flask import Blueprint, jsonify, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from utils import token_required, login_required

user = Blueprint('user', __name__)


@user.route('/login')
def login():
    from main import oauth
    google = oauth.create_client('google')  # create the google oauth client
    redirect_uri = url_for('user.authorize', _external=True)
    return google.authorize_redirect(redirect_uri)


@user.route('/authorize')
def authorize():
    from main import oauth
    google = oauth.create_client('google')  # create the google oauth client
    token = google.authorize_access_token()  # Access token from google (needed to get user info)
    resp = google.get('userinfo')  # userinfo contains stuff u specificed in the scrope
    user_info = resp.json()
    user = oauth.google.userinfo()  # uses openid endpoint to fetch user info
    # Here you use the profile/user data that you got and query your database find/register the user
    # and set ur own data in the session not the profile from google
    session['profile'] = user_info
    session.permanent = True  # make the session permanant so it keeps existing after broweser gets closed
    return jsonify({"success": True, "token": token}), 200


@user.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return jsonify({"success": True, "message": "Logged out succesfully"}), 200


@user.post('/signup')
def signup():
    from main import db
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


@user.put('/user/<user_id>/')
@token_required
def update_user_by_id(current_user, user_id):
    from main import db
    user_from_db = db.session.query(User).filter_by(id=user_id).first()
    if not user_from_db:
        return jsonify({'success': False, 'message': 'No user found!'})
    if current_user.user_type in [3, 4] and current_user.id != int(user_id):
        return jsonify({"success": False,
                        "message": "User cannot update different user details, unless it is admin/trainer"}), 401
    data = flask.request.json
    try:
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
            if key == 'user_type':
                user_from_db.user_type = data['user_type']
        db.session.commit()
        return jsonify({"success": True, "user": user_from_db.to_dict()})
    except:
        return jsonify({"success": False, "message": "Something went wrong"}), 400


@user.delete('/user/<user_id>/')
@token_required
def delete_user(current_user, user_id):
    from main import db
    user_to_delete = db.session.query(User).filter_by(id=user_id).first()
    if not user_to_delete:
        return jsonify({'success': False, 'message': 'No user found!'})
    if current_user.user_type != 1:
        return jsonify({"success": False,
                        "message": "User cannot delete users, unless it is admin"}), 401
    db.session.delete(user_to_delete)
    db.session.commit()
    return jsonify({"success": True,
                    "message": "User: " + user_id + " was deleted successfully"}), 200


@user.get('/user/<user_id>/')
@token_required
def get_user(current_user, user_id):
    from main import db
    user_from_db = db.session.query(User).filter_by(id=user_id).first()
    if not user_from_db:
        return jsonify({'success': False, 'message': 'No user found!'})
    if current_user.user_type in [3, 4] and current_user.id != int(user_id):
        return jsonify({"success": False,
                        "message": "User cannot view different user details, unless it is admin/trainer"}), 401
    return jsonify({'success': True, 'user': user_from_db.to_dict()})

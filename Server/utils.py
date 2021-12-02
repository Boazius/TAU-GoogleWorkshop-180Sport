from functools import wraps
import jwt
from flask import request, jsonify, session
from models import User


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        from main import db
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, options={"verify_signature": False})
            print(data)
            current_user = db.session.query(User).filter_by(email=data['email']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        from main import db
        user = dict(session).get('profile', None)
        print(user)
        try:
            db_user = db.session.query(User).filter_by(email=dict(session)['profile']['email']).first()
        except:
            db_user = None
        print(db_user)
        if user and db_user:
            return f(db_user, *args, **kwargs)
        return jsonify({'message': 'Please login before performing this action!'}), 401

    return decorated_function

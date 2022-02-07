from functools import wraps
import jwt
from flask import request, jsonify, session
from models import User
import google
from google.auth.transport import requests
from google.oauth2 import id_token


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
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), "919619848127-0d5ata8oi64g4neesm7vss0cb30evnph.apps.googleusercontent.com")
            print(idinfo)
            current_user = db.session.query(User).filter_by(email=idinfo['email']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        from main import db
        db_user = None
        if 'secret-code' in request.headers:
            if request.headers['secret-code'] == 'G6kdi6pN0AFxo01x':
                db_user = db.session.query(User).filter_by(id=1).first()
            return f(db_user, *args, **kwargs)
        return jsonify({'message': 'Please login before performing this action!'}), 401
    return decorated_function

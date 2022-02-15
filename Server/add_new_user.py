from main import db
from models import User, User_type, Training, Group
from datetime import datetime, date
from flask import Blueprint, jsonify

current_user = db.session.query(User).filter_by(email="dana").first()
print(current_user)

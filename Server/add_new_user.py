from main import db
from models import User, User_type


print(db.session.query(User).filter_by(user_type=1).first().to_dict())
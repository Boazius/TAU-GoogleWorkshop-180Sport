from flask_sqlalchemy import SQLAlchemy
from application import create_app
from models import User
from models import User_type

app = create_app()
db = SQLAlchemy(app)
# session = Session(bind=engine)



@app.route("/hello")
def hello():
    user = db.session.query(User_type).all()
    if not user:
        return str(1)
    return "HI"


@app.get('/users/group_id/<group_id>/')
def get_all_users_by_group_id(group_id):
    for user in db.session.query(User):
        group_ids = user.group_ids
        print(type(group_ids))
    return "HELLO"


if __name__ == '__main__':
    app.run()


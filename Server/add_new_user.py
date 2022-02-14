from main import db
from models import User, User_type, Training
from datetime import datetime, timedelta

trainings_from_db = db.session.query(Training).all()
list_of_dates = []
for training in trainings_from_db:
    if training.group_id == 3:
        if training.date < datetime.today().date():
            list_of_dates.append(training.date)

print(datetime.now().isoweekday())
today = datetime.now()
idx = (today.weekday() + 1) % 7
print(today - timedelta(days=7+idx))
print(datetime.now() - timedelta(days=((datetime.now().isoweekday()) % 7)))

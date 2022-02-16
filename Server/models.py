"""
models.py
- Data classes for the surveyapi application
"""
import json
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, \
    create_engine, ForeignKeyConstraint, \
    CheckConstraint, inspect


Base = declarative_base()
engine = create_engine("mysql+pymysql://root:G6kdi6pN0AFxo01x@35.240.11.106/db180", echo=True)
Session = sessionmaker()


class User(Base):
    __tablename__ = 'users'
    __tableargs__ = (CheckConstraint('user_type IN (1, 2, 3, 4)'),
                     CheckConstraint('NOT(trainings_ids IS NULL)'))
    id = Column(Integer(), primary_key=True, unique=True, autoincrement=True)
    user_type = Column(Integer(), ForeignKey("user_types.id"))
    email = Column(String(50), unique=True)
    full_name = Column(String(50))
    phone_number = Column(String(20))
    group_ids = Column(String(30))
    training_ids = Column(String(500))
    #attendance = Column(Integer(), ForeignKey("attendance_options.id"))
    active_or_not = Column(Boolean())

    def to_dict(self):
        columns = self.__table__.columns.keys()
        ret_data = {}
        for key in columns:
            ret_data[key] = getattr(self, key)
        return ret_data


class User_type(Base):
    __tablename__ = 'user_types'
    id = Column(Integer(), primary_key=True, unique=True)
    name = Column(String(30))


class Group(Base):
    __tablename__= 'groups'
    id = Column(Integer(), primary_key=True, unique=True, autoincrement=True)
    day = Column(String(15), nullable=False)
    time = Column(String(15), nullable=False)
    meeting_place = Column(String(50), nullable=False)
    trainings_list = Column(String(500))
    active_or_not = Column(Boolean(), nullable=False)

    def to_dict(self):
        columns = self.__table__.columns.keys()
        ret_data = {}
        for key in columns:
            if key == "trainings_list":
                if getattr(self, key) is not None and getattr(self, key) != "":
                    ret_data[key] = str(getattr(self, key)).split(',')
                else:
                    ret_data[key] = []
            else:
                ret_data[key] = getattr(self, key)
        return ret_data



class Training(Base):
    __tablename__ = 'trainings'
    id = Column(Integer(), primary_key=True, unique=True, autoincrement=True)
    group_id = Column(Integer(), ForeignKey("groups.id"), nullable=False)
    date = Column(Date(), nullable=False)
    day = Column(String(15), nullable=False)
    time = Column(String(50), nullable=False)
    meeting_place = Column(String(50), nullable=False)
    attendance_users = Column(String(7000)) #dict
    is_happened = Column(Boolean())
    trainers_id = Column(String(100)) #list
    notes = Column(String(7500)) #dict
    trainer_notes = Column(String(7000)) #dict


    def to_dict(self):
        columns = self.__table__.columns.keys()
        ret_data = {}
        for key in columns:
            if key == "trainers_id":
                if getattr(self, key) is not None:
                    ret_data[key] = str(getattr(self, key)).split(',')
                else:
                    ret_data[key] = getattr(self, key)
            elif key == "attendance_users" or key == "notes" or key == "trainer_notes":
                if getattr(self, key) is not None:
                    ret_data[key] = json.loads(getattr(self, key))
                else:
                    ret_data[key] = getattr(self, key)
            elif key == "date":
                ret_data[key] = getattr(self, key)

            else:
                ret_data[key] = getattr(self, key)
        return ret_data



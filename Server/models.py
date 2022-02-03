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
engine = create_engine('sqlite:///180.db', echo=True)
Session = sessionmaker()


class User(Base):
    __tablename__ = 'users'
    __tableargs__ = (CheckConstraint('user_type IN (1, 2, 3, 4)'),
                     CheckConstraint('NOT(trainings_ids IS NULL)'))
    id = Column(Integer(), primary_key=True, unique=True, autoincrement=True)
    user_type = Column(Integer(), ForeignKey("user_types.id"))
    email = Column(String(), unique=True)
    full_name = Column(String())
    phone_number = Column(String())
    group_ids = Column(String())
    training_ids = Column(String())
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
    name = Column(String())


class Group(Base):
    __tablename__= 'groups'
    id = Column(Integer(), primary_key=True, unique=True, autoincrement=True)
    day = Column(Integer(), nullable=False)
    time = Column(String(), nullable=False)
    meeting_place = Column(String(), nullable=False)
    trainings_list = Column(String())
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
    day = Column(Integer(), nullable=False)
    time = Column(String(), nullable=False)
    meeting_place = Column(String(), nullable=False)
    attendance_users = Column(String()) #dict
    is_happened = Column(Boolean())
    trainers_id = Column(Integer()) #list
    notes = Column(String()) #dict
    trainer_notes = Column(String()) #dict


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



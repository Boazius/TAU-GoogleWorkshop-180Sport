"""
models.py
- Data classes for the surveyapi application
"""

from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, create_engine

Base = declarative_base()
engine = create_engine('sqlite:///180.db', echo=True)
Session = sessionmaker()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True, unique=True, autoincrement=True)
    user_type = Column(Integer(), ForeignKey("user_types.id"))
    email = Column(String(), unique=True)
    password = Column(String())
    full_name = Column(String())
    phone_number = Column(String())
    group_ids = Column(String())
    training_ids = Column(String())
    attendance = Column(Integer(), ForeignKey("attendance_options.id"))
    active_or_not = Column(Boolean())

    def to_dict(self):
        columns = self.__table__.columns.keys()
        ret_data = {}
        for key in columns:
            if key != 'password':
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
    trainers_list = Column(String())
    trainees_list = Column(String())
    volunteers_list = Column(String())
    training_ids = Column(String())
    training_ids_list = Column(String())
    active_or_not = Column(Boolean(), nullable=False)


class Training(Base):
    __tablename__ = 'trainings'
    id = Column(Integer(), primary_key=True, unique=True, autoincrement=True)
    group_id = Column(Integer(), ForeignKey("groups.id"), nullable=False)
    date = Column(DateTime(), nullable=False)
    meeting_place = Column(String(), nullable=False)
    attendance_users = Column(String())
    is_happened = Column(Boolean())
    trainer_id = Column(Integer(), ForeignKey("users.id"), nullable=False)
    notes = Column(String())


class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer(), primary_key=True, unique=True, autoincrement=True)
    user_id = Column(Integer(), ForeignKey("users.id"), nullable=False)
    training_id = Column(Integer(), ForeignKey("trainings.id"), nullable=False)
    test = Column(String(), nullable=False)
    date = Column(DateTime())


class Attendance_options(Base):
    __tablename__ = 'attendance_options'
    id = Column(Integer(), primary_key=True, unique=True, autoincrement=True)
    name = Column(String())

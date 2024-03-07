from sqlalchemy import Table, Column, Integer, String, MetaData, DateTime
from sqlalchemy.ext.declarative import declarative_base
metadata_obj = MetaData()
from datetime import datetime

Base = declarative_base()
now = datetime.utcnow

class Subscribers(Base):
    __tablename__ = 'subscribers'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    good_id = Column(Integer)


class History(Base):
    __tablename__ = 'request_history'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    req_date = Column(DateTime(), default=datetime.now)
    good_id = Column(Integer)

subscribers_table = Table(
    'subscribers',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer),
    Column('good_id', Integer)
)

history_table = Table(
    'history',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer),
    Column('req_date', DateTime, default=now),
    Column('good_id', Integer)
)
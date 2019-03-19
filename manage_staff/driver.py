import sqlite3
import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

driver_engine = create_engine('sqlite:///staff.db', echo=False)
driver_base = declarative_base()
driver_session = sessionmaker(bind=driver_engine)

class driver(driver_base):
    __tablename__ = 'drivers'
    name = Column(String, primary_key=True)
    in_stream = Column(String)
    has_class_IV = Column(String)
    four_hour = Column(String)
    c_wave = Column(String)
    full_day = Column(String)
    scenic_float = Column(String)
    overnight = Column(String)
    four_hour_seniority = Column(Integer)
    c_wave_seniority = Column(Integer)
    full_day_seniority = Column(Integer)
    scenic_float_seniority = Column(Integer)
    overnight_seniority = Column(Integer)
    driven_this_summer_four_hour = Column(Integer)
    driven_this_summer_c_wave = Column(Integer)
    driven_this_summer_full_day = Column(Integer)
    driven_this_summer_scenic_float = Column(Integer)
    driven_this_summer_overnight = Column(Integer)
    driven_this_period_four_hour = Column(Integer)
    driven_this_period_c_wave = Column(Integer)
    driven_this_period_full_day = Column(Integer)
    driven_this_period_scenic_float = Column(Integer)
    driven_this_period_overnight = Column(Integer)
    days_since_last_day_off = Column(Integer)

driver_base.metadata.create_all(driver_engine)

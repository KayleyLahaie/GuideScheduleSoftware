import sqlite3
import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


guide_engine = create_engine('sqlite:///staff.db', echo=False)
guide_base = declarative_base()
guide_session = sessionmaker(bind=guide_engine)

class guide(guide_base):
    """
    Produces a guide object used for calculating trip and role priorities and
    tracking trips worked

    All attributes are column objects of either type string or integer and
    represent a column in the guide table of the staff.db file
    """
    
    __tablename__ = 'guides'
    name = Column(String, primary_key=True)
    in_stream = Column(String)
    has_class_IV = Column(String)
    tl_four_hour = Column(String)
    tl_c_wave = Column(String)
    tl_full_day = Column(String)
    tl_scenic_float = Column(String)
    tl_overnight = Column(String)
    guide_four_hour = Column(String)
    guide_c_wave = Column(String)
    guide_full_day = Column(String)
    guide_scenic_float = Column(String)
    guide_overnight = Column(String)
    safety_four_hour = Column(String)
    safety_c_wave = Column(String)
    safety_full_day = Column(String)
    safety_scenic_float = Column(String)
    safety_overnight = Column(String)
    tl_this_summer_four_hour = Column(Integer)
    tl_this_summer_c_wave = Column(Integer)
    tl_this_summer_full_day = Column(Integer)
    tl_this_summer_scenic_float = Column(Integer)
    tl_this_summer_overnight = Column(Integer)
    tl_this_period_four_hour = Column(Integer)
    tl_this_period_c_wave = Column(Integer)
    tl_this_period_full_day = Column(Integer)
    tl_this_period_scenic_float = Column(Integer)
    tl_this_period_overnight = Column(Integer)
    guided_this_summer_four_hour = Column(Integer)
    guided_this_summer_c_wave = Column(Integer)
    guided_this_summer_full_day = Column(Integer)
    guided_this_summer_scenic_float = Column(Integer)
    guided_this_summer_overnight = Column(Integer)
    guided_this_period_four_hour = Column(Integer)
    guided_this_period_c_wave = Column(Integer)
    guided_this_period_full_day = Column(Integer)
    guided_this_period_scenic_float = Column(Integer)
    guided_this_period_overnight = Column(Integer)
    safety_this_summer_four_hour = Column(Integer)
    safety_this_summer_c_wave = Column(Integer)
    safety_this_summer_full_day = Column(Integer)
    safety_this_summer_scenic_float = Column(Integer)
    safety_this_summer_overnight = Column(Integer)
    safety_this_period_four_hour = Column(Integer)
    safety_this_period_c_wave = Column(Integer)
    safety_this_period_full_day = Column(Integer)
    safety_this_period_scenic_float = Column(Integer)
    safety_this_period_overnight = Column(Integer)
    days_since_last_day_off = Column(Integer)

guide_base.metadata.create_all(guide_engine)

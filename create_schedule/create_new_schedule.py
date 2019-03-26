import sqlite3
import sqlalchemy

import excel_scraper

import create_schedule
from create_schedule import schedule_util
from create_schedule import schedule_dictionaries
from create_schedule import get_priority

import manage_staff
from manage_staff import guide
from manage_staff import driver

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import load_only

schedule_engine = create_engine('sqlite:///trips.db', echo=False)
schedule_base = declarative_base()
schedule_session = sessionmaker(bind=schedule_engine)

session_schedule = schedule_session()
session_guide = guide.guide_session()
session_driver = driver.driver_session()


class schedule(schedule_base):

    __tablename__ = 'schedule'
    date = Column(String, primary_key=True)
    _ready_set_go_10_tentative = Column(String)
    _ready_set_go_14_tentative = Column(String)
    _c_wave_10_tentative = Column(String)
    _c_wave_14_tentative = Column(String)
    _guaranteed_addiction_930_tentative = Column(String)
    _scenic_float_09_tentative = Column(String)
    _scenic_float_13_tentative = Column(String)
    num_clients_ready_set_go_10 = Column(Integer)
    num_guides_ready_set_go_10 = Column(Integer)
    num_safety_ready_set_go_10 = Column(Integer)
    num_drivers_ready_set_go_10 = Column(Integer)
    trip_leader_ready_set_go_10 = Column(String)
    second_guide_ready_set_go_10 = Column(String)
    third_guide_ready_set_go_10 = Column(String)
    fourth_guide_ready_set_go_10 = Column(String)
    fifth_guide_ready_set_go_10 = Column(String)
    safety_ready_set_go_10 = Column(String)
    first_driver_ready_set_go_10 = Column(String)
    second_driver_ready_set_go_10 = Column(String)
    num_clients_ready_set_go_14 = Column(Integer)
    num_guides_ready_set_go_14 = Column(Integer)
    num_safety_ready_set_go_14 = Column(Integer)
    num_drivers_ready_set_go_14 = Column(Integer)
    trip_leader_ready_set_go_14 = Column(String)
    second_guide_ready_set_go_14 = Column(String)
    third_guide_ready_set_go_14 = Column(String)
    fourth_guide_ready_set_go_14 = Column(String)
    fifth_guide_ready_set_go_14 = Column(String)
    safety_ready_set_go_14 = Column(String)
    first_driver_ready_set_go_14 = Column(String)
    second_driver_ready_set_go_14 = Column(String)
    num_clients_c_wave_10 = Column(Integer)
    num_guides_c_wave_10 = Column(Integer),
    num_safety_c_wave_10 = Column(Integer),
    num_drivers_c_wave_10 = Column(Integer),
    trip_leader_c_wave_10 = Column(String)
    second_guide_c_wave_10 = Column(String)
    third_guide_c_wave_10 = Column(String)
    fourth_guide_c_wave_10 = Column(String)
    fifth_guide_c_wave_10 = Column(String)
    safety_c_wave_10 = Column(String)
    first_driver_c_wave_10 = Column(String)
    second_driver_c_wave_10 = Column(String)
    num_clients_c_wave_14 = Column(Integer)
    num_guides_c_wave_14 = Column(Integer)
    num_safety_c_wave_14 = Column(Integer)
    num_drivers_c_wave_14 = Column(Integer)
    trip_leader_c_wave_14 = Column(String)
    second_guide_c_wave_14 = Column(String)
    third_guide_c_wave_14 = Column(String)
    fourth_guide_c_wave_14 = Column(String)
    fifth_guide_c_wave_14 = Column(String)
    safety_c_wave_14 = Column(String)
    first_driver_c_wave_14 = Column(String)
    second_driver_c_wave_14 = Column(String)
    num_clients_guaranteed_addiction_930 = Column(Integer)
    num_guides_guaranteed_addiction_930 = Column(Integer)
    num_safety_guaranteed_addiction_930 = Column(Integer)
    num_drivers_guaranteed_addiction_930 = Column(Integer)
    trip_leader_guaranteed_addiction_930 = Column(String)
    second_guide_guaranteed_addiction_930 = Column(String)
    third_guide_guaranteed_addiction_930 = Column(String)
    fourth_guide_guaranteed_addiction_930 = Column(String)
    fifth_guide_guaranteed_addiction_930 = Column(String)
    safety_guaranteed_addiction_930 = Column(String)
    first_driver_guaranteed_addiction_930 = Column(String)
    second_driver_guaranteed_addiction_930 = Column(String)
    num_clients_scenic_float_09 = Column(Integer)
    num_guides_scenic_float_09 = Column(Integer)
    num_safety_scenic_float_09 = Column(Integer)
    num_drivers_scenic_float_09 = Column(Integer)
    trip_leader_scenic_float_09 = Column(String)
    second_guide_scenic_float_09 = Column(String)
    third_guide_scenic_float_09 = Column(String)
    fourth_guide_scenic_float_09 = Column(String)
    fifth_guide_scenic_float_09 = Column(String)
    safety_scenic_float_09 = Column(String)
    first_driver_scenic_float_09 = Column(String)
    second_driver_scenic_float_09 = Column(String)
    num_clients_scenic_float_13 = Column(Integer)
    num_guides_scenic_float_13 = Column(Integer)
    num_safety_scenic_float_13 = Column(Integer)
    num_drivers_scenic_float_13 = Column(Integer)
    trip_leader_scenic_float_13 = Column(String)
    second_guide_scenic_float_13 = Column(String)
    third_guide_scenic_float_13 = Column(String)
    fourth_guide_scenic_float_13 = Column(String)
    fifth_guide_scenic_float_13 = Column(String)
    safety_scenic_float_13 = Column(String)
    first_driver_scenic_float_13 = Column(String)
    second_driver_scenic_float_13 = Column(String)
    num_clients_overnight_930 = Column(Integer)
    num_guides_overnight_930 = Column(Integer)
    num_safety_overnight_930 = Column(Integer)
    num_drivers_overnight_930 = Column(Integer)
    trip_leader_overnight_930 = Column(String)
    second_guide_overnight_930 = Column(String)
    third_guide_overnight_930 = Column(String)
    fourth_guide_overnight_930 = Column(String)
    fifth_guide_overnight_930 = Column(String)
    safety_overnight_930 = Column(String)
    first_driver_overnight_930 = Column(String)
    second_driver_overnight_930 = Column(String)


def add_new_date(current_date):

    schedule_object = session_schedule.query(schedule).filter(
                            schedule.date == current_date)

    schedule_list = [u.__dict__ for u in schedule_object.all()]

    if schedule_list:
        for trip in create_schedule.schedule_dictionaries.trip_switch_excel:
            for role in create_schedule.schedule_dictionaries.role_switch:
                staff_member = schedule_list[0][
                                    create_schedule.schedule_dictionaries.role_switch[role]
                                    +create_schedule.schedule_dictionaries.trip_switch_excel[trip]
                                ]
                if staff_member:
                    if role <= 4:

                        manage_staff.staff_util.update_num_trips_guide(
                                                    staff_member,
                                                    create_schedule.schedule_dictionaries.max_guides_trip_swictch[trip],
                                                    -1,
                                                    create_schedule.schedule_dictionaries.guide_roles_converter[role]
                                                )
                    else:
                        manage_staff.staff_util.update_num_trips_driver(
                                                    staff_member,
                                                    create_schedule.schedule_dictionaries.max_guides_trip_swictch[trip],
                                                    -1)

        session_schedule.query(schedule).filter(
                    schedule.date == current_date
                ).delete(synchronize_session=False)

        session_schedule.commit()



    current_date_object = schedule( date = current_date,
                                        _ready_set_go_10_tentative = '',
                                        _ready_set_go_14_tentative = '',
                                        _c_wave_10_tentative = '',
                                        _c_wave_14_tentative = '',
                                        _guaranteed_addiction_930_tentative = '',
                                        _scenic_float_09_tentative = '',
                                        _scenic_float_13_tentative = '',
                                        num_clients_ready_set_go_10 = 0,
                                        num_guides_ready_set_go_10 = 0,
                                        num_safety_ready_set_go_10 = 0,
                                        num_drivers_ready_set_go_10 = 0,
                                        trip_leader_ready_set_go_10 = '',
                                        second_guide_ready_set_go_10 = '',
                                        third_guide_ready_set_go_10 = '',
                                        fourth_guide_ready_set_go_10 = '',
                                        fifth_guide_ready_set_go_10 = '',
                                        safety_ready_set_go_10 = '',
                                        first_driver_ready_set_go_10 = '',
                                        second_driver_ready_set_go_10 = '',
                                        num_clients_ready_set_go_14 = 0,
                                        num_guides_ready_set_go_14 = 0,
                                        num_safety_ready_set_go_14 = 0,
                                        num_drivers_ready_set_go_14 = 0,
                                        trip_leader_ready_set_go_14 = '',
                                        second_guide_ready_set_go_14 = '',
                                        third_guide_ready_set_go_14 = '',
                                        fourth_guide_ready_set_go_14 = '',
                                        fifth_guide_ready_set_go_14 = '',
                                        safety_ready_set_go_14 = '',
                                        first_driver_ready_set_go_14 = '',
                                        second_driver_ready_set_go_14 = '',
                                        num_clients_c_wave_10 = 0,
                                        num_guides_c_wave_10 = 0,
                                        num_safety_c_wave_10 = 0,
                                        num_drivers_c_wave_10 = 0,
                                        trip_leader_c_wave_10 = '',
                                        second_guide_c_wave_10 = '',
                                        third_guide_c_wave_10 = '',
                                        fourth_guide_c_wave_10 = '',
                                        fifth_guide_c_wave_10 = '',
                                        safety_c_wave_10 = '',
                                        first_driver_c_wave_10 = '',
                                        second_driver_c_wave_10 = '',
                                        num_clients_c_wave_14 = 0,
                                        num_guides_c_wave_14 = 0,
                                        num_safety_c_wave_14 = 0,
                                        num_drivers_c_wave_14 = 0,
                                        trip_leader_c_wave_14 = '',
                                        second_guide_c_wave_14 = '',
                                        third_guide_c_wave_14 = '',
                                        fourth_guide_c_wave_14 = '',
                                        fifth_guide_c_wave_14 = '',
                                        safety_c_wave_14 = '',
                                        first_driver_c_wave_14 = '',
                                        second_driver_c_wave_14 = '',
                                        num_clients_guaranteed_addiction_930 = 0,
                                        num_guides_guaranteed_addiction_930 = 0,
                                        num_safety_guaranteed_addiction_930 = 0,
                                        num_drivers_guaranteed_addiction_930 = 0,
                                        trip_leader_guaranteed_addiction_930 = '',
                                        second_guide_guaranteed_addiction_930 = '',
                                        third_guide_guaranteed_addiction_930 = '',
                                        fourth_guide_guaranteed_addiction_930 = '',
                                        fifth_guide_guaranteed_addiction_930 = '',
                                        safety_guaranteed_addiction_930 = '',
                                        first_driver_guaranteed_addiction_930 = '',
                                        second_driver_guaranteed_addiction_930 = '',
                                        num_clients_scenic_float_09 = 0,
                                        num_guides_scenic_float_09 = 0,
                                        num_safety_scenic_float_09 = 0,
                                        num_drivers_scenic_float_09 = 0,
                                        trip_leader_scenic_float_09 = '',
                                        second_guide_scenic_float_09 = '',
                                        third_guide_scenic_float_09 = '',
                                        fourth_guide_scenic_float_09 = '',
                                        fifth_guide_scenic_float_09 = '',
                                        safety_scenic_float_09 = '',
                                        first_driver_scenic_float_09 = '',
                                        num_clients_scenic_float_13 = 0,
                                        num_guides_scenic_float_13 = 0,
                                        num_safety_scenic_float_13 = 0,
                                        num_drivers_scenic_float_13 = 0,
                                        trip_leader_scenic_float_13 = '',
                                        second_guide_scenic_float_13 = '',
                                        third_guide_scenic_float_13 = '',
                                        fourth_guide_scenic_float_13 = '',
                                        fifth_guide_scenic_float_13 = '',
                                        safety_scenic_float_13 = '',
                                        first_driver_scenic_float_13 = '',
                                        second_driver_scenic_float_13 = '',
                                        num_clients_overnight_930 = 0,
                                        num_guides_overnight_930 = 0,
                                        num_safety_overnight_930 = 0,
                                        num_drivers_overnight_930 = 0,
                                        trip_leader_overnight_930 = '',
                                        second_guide_overnight_930 = '',
                                        third_guide_overnight_930 = '',
                                        fourth_guide_overnight_930 = '',
                                        fifth_guide_overnight_930 = '',
                                        safety_overnight_930 = '',
                                        first_driver_overnight_930 = '',
                                        second_driver_overnight_930 = '')

    session_schedule.add(current_date_object)
    session_schedule.commit()

    return current_date_object


def submit_to_database(trip_role_assignment_final, num_drivers, num_clients,
                       num_guides, num_safety, current_date_object,
                       current_date):

    current_date_object.date = current_date
    current_date_object._ready_set_go_10_tentative = ''
    current_date_object._ready_set_go_14_tentative = ''
    current_date_object._c_wave_10_tentative = ''
    current_date_object._c_wave_14_tentative = ''
    current_date_object._guaranteed_addiction_930_tentative = ''
    current_date_object._scenic_float_09_tentative = ''
    current_date_object._scenic_float_13_tentative = ''
    current_date_object.num_clients_ready_set_go_10 = num_clients['Ready Set Go - 4 Hour - 10:00:00']
    current_date_object.num_guides_ready_set_go_10 = num_guides['Ready Set Go - 4 Hour - 10:00:00']
    current_date_object.num_safety_ready_set_go_10 = num_safety
    current_date_object.num_drivers_ready_set_go_10 = num_drivers['Ready Set Go - 4 Hour - 10:00:00']
    current_date_object.trip_leader_ready_set_go_10 = trip_role_assignment_final['trip_leader_ready_set_go_10']
    current_date_object.second_guide_ready_set_go_10 = trip_role_assignment_final['second_guide_ready_set_go_10']
    current_date_object.third_guide_ready_set_go_10 = trip_role_assignment_final['third_guide_ready_set_go_10']
    current_date_object.fourth_guide_ready_set_go_10 = trip_role_assignment_final['fourth_guide_ready_set_go_10']
    current_date_object.fifth_guide_ready_set_go_10 = ''
    current_date_object.safety_ready_set_go_10 = trip_role_assignment_final['safety_ready_set_go_10']
    current_date_object.first_driver_ready_set_go_10 = trip_role_assignment_final['first_driver_ready_set_go_10']
    current_date_object.second_driver_ready_set_go_10 = trip_role_assignment_final['second_driver_ready_set_go_10']
    current_date_object.num_clients_ready_set_go_14 = num_clients['Ready Set Go - 4 Hour - 14:00:00']
    current_date_object.num_guides_ready_set_go_14 = num_guides['Ready Set Go - 4 Hour - 14:00:00']
    current_date_object.num_safety_ready_set_go_14 = num_safety
    current_date_object.num_drivers_ready_set_go_14 = num_drivers['Ready Set Go - 4 Hour - 14:00:00']
    current_date_object.trip_leader_ready_set_go_14 = trip_role_assignment_final['trip_leader_ready_set_go_14']
    current_date_object.second_guide_ready_set_go_14 = trip_role_assignment_final['second_guide_ready_set_go_14']
    current_date_object.third_guide_ready_set_go_14 = trip_role_assignment_final['third_guide_ready_set_go_14']
    current_date_object.fourth_guide_ready_set_go_14 = trip_role_assignment_final['fourth_guide_ready_set_go_14']
    current_date_object.fifth_guide_ready_set_go_14 = ''
    current_date_object.safety_ready_set_go_14 = trip_role_assignment_final['safety_ready_set_go_14']
    current_date_object.first_driver_ready_set_go_14 = trip_role_assignment_final['first_driver_ready_set_go_14']
    current_date_object.second_driver_ready_set_go_14 = trip_role_assignment_final['second_driver_ready_set_go_14']
    current_date_object.num_clients_c_wave_10 = num_clients['Catch A Wave - 10:00:00']
    current_date_object.num_guides_c_wave_10 = num_guides['Catch A Wave - 10:00:00']
    current_date_object.num_safety_c_wave_10 = num_safety
    current_date_object.num_drivers_c_wave_10 = num_drivers['Catch A Wave - 10:00:00']
    current_date_object.trip_leader_c_wave_10 = trip_role_assignment_final['trip_leader_c_wave_10']
    current_date_object.second_guide_c_wave_10 = trip_role_assignment_final['second_guide_c_wave_10']
    current_date_object.third_guide_c_wave_10 = trip_role_assignment_final['third_guide_c_wave_10']
    current_date_object.fourth_guide_c_wave_10 = trip_role_assignment_final['fourth_guide_c_wave_10']
    current_date_object.fifth_guide_c_wave_10 = ''
    current_date_object.safety_c_wave_10 = trip_role_assignment_final['safety_c_wave_10']
    current_date_object.first_driver_c_wave_10 = trip_role_assignment_final['first_driver_c_wave_10']
    current_date_object.second_driver_c_wave_10 = trip_role_assignment_final['second_driver_c_wave_10']
    current_date_object.num_clients_c_wave_14 = num_clients['Catch A Wave - 14:00:00']
    current_date_object.num_guides_c_wave_14 = num_guides['Catch A Wave - 14:00:00']
    current_date_object.num_safety_c_wave_14 = num_safety
    current_date_object.num_drivers_c_wave_14 = num_drivers['Catch A Wave - 14:00:00']
    current_date_object.trip_leader_c_wave_14 = trip_role_assignment_final['trip_leader_c_wave_14']
    current_date_object.second_guide_c_wave_14 = trip_role_assignment_final['second_guide_c_wave_14']
    current_date_object.third_guide_c_wave_14 = trip_role_assignment_final['third_guide_c_wave_14']
    current_date_object.fourth_guide_c_wave_14 = trip_role_assignment_final['fourth_guide_c_wave_14']
    current_date_object.fifth_guide_c_wave_14 = ''
    current_date_object.safety_c_wave_14 = trip_role_assignment_final['safety_c_wave_14']
    current_date_object.first_driver_c_wave_14 = trip_role_assignment_final['first_driver_c_wave_14']
    current_date_object.second_driver_c_wave_14 = trip_role_assignment_final['second_driver_c_wave_14']
    current_date_object.num_clients_guaranteed_addiction_930 = num_clients['Guaranteed Addiction - 09:30:00']
    current_date_object.num_guides_guaranteed_addiction_930 = num_guides['Guaranteed Addiction - 09:30:00']
    current_date_object.num_safety_guaranteed_addiction_930 = num_safety
    current_date_object.num_drivers_guaranteed_addiction_930 = num_drivers['Guaranteed Addiction - 09:30:00']
    current_date_object.trip_leader_guaranteed_addiction_930 = trip_role_assignment_final['trip_leader_guaranteed_addiction_930']
    current_date_object.second_guide_guaranteed_addiction_930 = trip_role_assignment_final['second_guide_guaranteed_addiction_930']
    current_date_object.third_guide_guaranteed_addiction_930 = trip_role_assignment_final['third_guide_guaranteed_addiction_930']
    current_date_object.fourth_guide_guaranteed_addiction_930 = trip_role_assignment_final['fourth_guide_guaranteed_addiction_930']
    current_date_object.fifth_guide_guaranteed_addiction_930 = ''
    current_date_object.safety_guaranteed_addiction_930 = trip_role_assignment_final['safety_guaranteed_addiction_930']
    current_date_object.first_driver_guaranteed_addiction_930 = trip_role_assignment_final['first_driver_guaranteed_addiction_930']
    current_date_object.second_driver_guaranteed_addiction_930 = trip_role_assignment_final['second_driver_guaranteed_addiction_930']
    current_date_object.num_clients_scenic_float_09 = num_clients['Take it Easy - Scenic Float - 09:00:00']
    current_date_object.num_guides_scenic_float_09 = num_guides['Take it Easy - Scenic Float - 09:00:00']
    current_date_object.num_safety_scenic_float_09 = num_safety
    current_date_object.num_drivers_scenic_float_09 = num_drivers['Take it Easy - Scenic Float - 09:00:00']
    current_date_object.trip_leader_scenic_float_09 = trip_role_assignment_final['trip_leader_scenic_float_09']
    current_date_object.second_guide_scenic_float_09 = trip_role_assignment_final['second_guide_scenic_float_09']
    current_date_object.third_guide_scenic_float_09 = trip_role_assignment_final['third_guide_scenic_float_09']
    current_date_object.fourth_guide_scenic_float_09 = trip_role_assignment_final['fourth_guide_scenic_float_09']
    current_date_object.fifth_guide_scenic_float_09 = ''
    current_date_object.safety_scenic_float_09 = trip_role_assignment_final['safety_scenic_float_09']
    current_date_object.first_driver_scenic_float_09 = trip_role_assignment_final['first_driver_scenic_float_09']
    current_date_object.num_clients_scenic_float_13 = num_clients['Take it Easy - Scenic Float - 13:00:00']
    current_date_object.num_guides_scenic_float_13 = num_guides['Take it Easy - Scenic Float - 13:00:00']
    current_date_object.num_safety_scenic_float_13 = num_safety
    current_date_object.num_drivers_scenic_float_13 = num_drivers['Take it Easy - Scenic Float - 13:00:00']
    current_date_object.trip_leader_scenic_float_13 = trip_role_assignment_final['trip_leader_scenic_float_13']
    current_date_object.second_guide_scenic_float_13 = trip_role_assignment_final['second_guide_scenic_float_13']
    current_date_object.third_guide_scenic_float_13 = trip_role_assignment_final['third_guide_scenic_float_13']
    current_date_object.fourth_guide_scenic_float_13 = trip_role_assignment_final['fourth_guide_scenic_float_13']
    current_date_object.fifth_guide_scenic_float_13 = ''
    current_date_object.safety_scenic_float_13 = ''
    current_date_object.first_driver_scenic_float_13 = trip_role_assignment_final['first_driver_scenic_float_13']
    current_date_object.second_driver_scenic_float_13 = trip_role_assignment_final['second_driver_scenic_float_13']
    current_date_object.num_clients_overnight_930 = num_clients['Ticket to Ride - 09:30:00']
    current_date_object.num_guides_overnight_930 = num_guides['Ticket to Ride - 09:30:00']
    current_date_object.num_safety_overnight_930 = num_safety
    current_date_object.num_drivers_overnight_930 = num_drivers['Ticket to Ride - 09:30:00']
    current_date_object.trip_leader_overnight_930 = trip_role_assignment_final['trip_leader_overnight_930']
    current_date_object.second_guide_overnight_930 = trip_role_assignment_final['second_guide_overnight_930']
    current_date_object.third_guide_overnight_930 = trip_role_assignment_final['third_guide_overnight_930']
    current_date_object.fourth_guide_overnight_930 = trip_role_assignment_final['fourth_guide_overnight_930']
    current_date_object.fifth_guide_overnight_930 = ''
    current_date_object.safety_overnight_930 = trip_role_assignment_final['safety_overnight_930']
    current_date_object.first_driver_overnight_930 = trip_role_assignment_final['first_driver_overnight_930']
    current_date_object.second_driver_overnight_930 = trip_role_assignment_final['second_driver_overnight_930']

    session_schedule.add(current_date_object)
    session_schedule.commit()

schedule_base.metadata.create_all(schedule_engine)

import sqlite3
import sqlalchemy
import manage_staff
import collections
import create_schedule
import excel_scraper
from create_schedule import schedule_util
from create_schedule import schedule_dictionaries
from create_schedule import get_priority
from manage_staff import guide
from manage_staff import driver

from PySide2 import QtCore, QtGui, QtWidgets

import popups
from popups import not_enough_guides_popup
from popups import overnight_popup

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import load_only

from shutil import copyfile
import datetime
import time

import sys
import os

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

################################################################################

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


################################################################################


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

################################################################################


def copy_schedule_role(trips, trip_role_assignment, num_drivers, num_safety,
                        num_clients, num_guides, max_guides, max_drivers, current_date_object,
                        current_date):

    trip_role_assignment_final = {}
    trip_roles_dictionary = {}

    print(num_guides)
    print("max ", max_guides)

    print(num_drivers)
    print("max ", max_drivers)

    for trip_name in trips:

        print("trip dict: ", trip_roles_dictionary)
        #print(num_guides[trip_name])

        if trip_name in num_guides:

            if(num_guides[trip_name] == max_guides[create_schedule.schedule_dictionaries.max_guides_trip_swictch[trip_name]]):

                for role in range(len(create_schedule.schedule_dictionaries.role_switch)):

                    if create_schedule.schedule_dictionaries.role_switch[role]+create_schedule.schedule_dictionaries.trip_types[
                                create_schedule.schedule_dictionaries.max_guides_trip_swictch[trip_name]
                            ] in trip_role_assignment:

                        trip_role_assignment_final[create_schedule.schedule_dictionaries.role_switch[role]
                            +create_schedule.schedule_dictionaries.trip_switch_numerical[
                                create_schedule.schedule_dictionaries.trip_number_switch[trip_name]
                                ]
                            ] = trip_role_assignment[create_schedule.schedule_dictionaries.role_switch[role]
                                    +create_schedule.schedule_dictionaries.trip_types[
                                        create_schedule.schedule_dictionaries.max_guides_trip_swictch[trip_name]
                                    ]
                                ]

                        trip_roles_dictionary[create_schedule.schedule_dictionaries.trip_types[
                                create_schedule.schedule_dictionaries.max_guides_trip_swictch[trip_name]
                            ]+str(role)
                        ] = trip_role_assignment_final[
                                create_schedule.schedule_dictionaries.role_switch[role]
                                +create_schedule.schedule_dictionaries.trip_switch_numerical[
                                    create_schedule.schedule_dictionaries.trip_number_switch[trip_name]
                                ]
                            ]

                        print("Role, update: ", role)
                        if(role <= 4):

                            manage_staff.staff_util.update_num_trips_guide(
                                trip_role_assignment[
                                    create_schedule.schedule_dictionaries.role_switch[role]
                                    +create_schedule.schedule_dictionaries.trip_types[
                                        create_schedule.schedule_dictionaries.max_guides_trip_swictch[trip_name]]],
                                create_schedule.schedule_dictionaries.max_guides_trip_swictch[trip_name],
                                1, create_schedule.schedule_dictionaries.role_update_switch[role]
                            )

                        else:
                            manage_staff.staff_util.update_num_trips_driver(
                                trip_role_assignment[
                                    create_schedule.schedule_dictionaries.role_switch[role]
                                    +create_schedule.schedule_dictionaries.trip_types[
                                        create_schedule.schedule_dictionaries.max_guides_trip_swictch[trip_name]]],
                                create_schedule.schedule_dictionaries.max_guides_trip_swictch[trip_name],
                                1
                            )

                    else:

                        trip_role_assignment_final[
                            create_schedule.schedule_dictionaries.role_switch[role]
                            +create_schedule.schedule_dictionaries.trip_switch_numerical[
                                create_schedule.schedule_dictionaries.trip_number_switch[trip_name]
                            ]
                        ] = ""

    for trip_name in trips:

        print(trip_roles_dictionary)

        if trip_name in num_guides:

            if(num_guides[trip_name] != max_guides[create_schedule.schedule_dictionaries.max_guides_trip_swictch[trip_name]]):

                if (num_guides[trip_name] <= 4 and num_guides[trip_name] > 1 ):

                    for role in range(num_guides[trip_name]):

                        trip_role_assignment_final[
                            create_schedule.schedule_dictionaries.role_switch[role]
                            +create_schedule.schedule_dictionaries.trip_switch_numerical[
                                create_schedule.schedule_dictionaries.trip_number_switch[
                                    trip_name
                                ]
                            ]
                        ]  = trip_roles_dictionary[
                                create_schedule.schedule_dictionaries.trip_types[
                                    create_schedule.schedule_dictionaries.max_guides_trip_swictch[
                                        trip_name
                                    ]
                                ]+str(role)
                            ]

                        manage_staff.staff_util.update_num_trips_guide(
                            trip_roles_dictionary[
                                create_schedule.schedule_dictionaries.trip_types[
                                    create_schedule.schedule_dictionaries.max_guides_trip_swictch[
                                        trip_name
                                    ]
                                ]+str(role)
                            ],
                            create_schedule.schedule_dictionaries.max_guides_trip_swictch[trip_name],
                            1,
                            create_schedule.schedule_dictionaries.role_update_switch[role]
                        )

                    for role in range(num_guides[trip_name], 7):

                        trip_role_assignment_final[
                            create_schedule.schedule_dictionaries.role_switch[role]
                            +create_schedule.schedule_dictionaries.trip_switch_numerical[
                                create_schedule.schedule_dictionaries.trip_number_switch[
                                    trip_name
                                ]
                            ]
                        ]  = ""
                else:
                    trip_role_assignment_final[
                        create_schedule.schedule_dictionaries.role_switch[0]
                        +create_schedule.schedule_dictionaries.trip_switch_numerical[
                            create_schedule.schedule_dictionaries.trip_number_switch[
                                trip_name
                            ]
                        ]
                    ]  = trip_roles_dictionary[
                            create_schedule.schedule_dictionaries.trip_types[
                                create_schedule.schedule_dictionaries.max_guides_trip_swictch[
                                    trip_name
                                ]
                            ]+str(0)
                        ]

                    for index in range(1,7):

                        trip_role_assignment_final[
                            create_schedule.schedule_dictionaries.role_switch[index]
                            +create_schedule.schedule_dictionaries.trip_switch_numerical[
                                create_schedule.schedule_dictionaries.trip_number_switch[
                                    trip_name
                                ]
                            ]
                        ] = ""


                    manage_staff.staff_util.update_num_trips_guide(
                        trip_roles_dictionary[
                            create_schedule.schedule_dictionaries.trip_types[
                                create_schedule.schedule_dictionaries.max_guides_trip_swictch[
                                    trip_name
                                ]
                            ]+str(0)
                        ],
                        create_schedule.schedule_dictionaries.max_guides_trip_swictch[trip_name],
                        1,
                        create_schedule.schedule_dictionaries.role_update_switch[0]
                    )

                    if(max_guides[create_schedule.schedule_dictionaries.max_guides_trip_swictch[trip_name]] > 1):

                        trip_role_assignment_final[
                            create_schedule.schedule_dictionaries.role_switch[4]
                            +create_schedule.schedule_dictionaries.trip_switch_numerical[
                                create_schedule.schedule_dictionaries.trip_number_switch[
                                    trip_name
                                ]
                            ]
                        ]  = trip_roles_dictionary[
                                create_schedule.schedule_dictionaries.trip_types[
                                    create_schedule.schedule_dictionaries.max_guides_trip_swictch[
                                        trip_name
                                    ]
                                ]+str(1)
                            ]

                        manage_staff.staff_util.update_num_trips_guide(
                            trip_roles_dictionary[
                                create_schedule.schedule_dictionaries.trip_types[
                                    create_schedule.schedule_dictionaries.max_guides_trip_swictch[
                                        trip_name
                                    ]
                                ]+str(1)
                            ],
                            create_schedule.schedule_dictionaries.max_guides_trip_swictch[trip_name],
                            1,
                            create_schedule.schedule_dictionaries.role_update_switch[4]
                        )

                    else:

                        if create_schedule.schedule_dictionaries.trip_types[
                                create_schedule.schedule_dictionaries.max_guides_trip_swictch[
                                    trip_name
                                ]
                            ]+str(4) != "scenic_float4":

                            trip_role_assignment_final[
                                create_schedule.schedule_dictionaries.role_switch[4]
                                +create_schedule.schedule_dictionaries.trip_switch_numerical[
                                    create_schedule.schedule_dictionaries.trip_number_switch[
                                        trip_name
                                    ]
                                ]
                            ]  = trip_roles_dictionary[
                                    create_schedule.schedule_dictionaries.trip_types[
                                        create_schedule.schedule_dictionaries.max_guides_trip_swictch[
                                            trip_name
                                        ]
                                    ]+str(4)
                                ]

                            manage_staff.staff_util.update_num_trips_guide(
                                trip_roles_dictionary[create_schedule.schedule_dictionaries.trip_types[
                                    create_schedule.schedule_dictionaries.max_guides_trip_swictch[
                                        trip_name
                                    ]
                                ]+str(4)],
                                create_schedule.schedule_dictionaries.max_guides_trip_swictch[trip_name],
                                1,
                                create_schedule.schedule_dictionaries.role_update_switch[4]
                            )

    print(trip_role_assignment_final)

    submit_to_database(trip_role_assignment_final, num_drivers, num_clients,
                        num_guides, num_safety,
                        current_date_object, current_date)

################################################################################


def create_schedule_day(gui_window, scraper_object, current_date):

    #copyfile('trips.db', 'trips_backup.db')
    #copyfile('staff.db', 'staff_backup.db')

    #try:
        day_of_week = int(datetime.datetime.strptime(current_date, '%Y-%m-%d').strftime('%w'))
        print("DAY OF WEEK: ", day_of_week)

        if day_of_week == 0:
            print("MAKING SCHEDULE FOR MONDAY")
            manage_staff.staff_util.reset_this_period()

        current_date_object = add_new_date(current_date)
        temp_guide = 0
        print("\n")
        print("Creating Schedule for ", current_date)
        trips = scraper_object.get_day(current_date)
        trip_role_assignment = {}
        class_IV_needed = {}
        num_clients = {}
        num_drivers = {}
        num_guides = {}
        max_drivers = [0,0,0,0,0,0,0,0]
        max_guides = [0,0,0,0,0,0,0,0]

        num_safety = 0

        previous_date = schedule_util.calculate_previous_date(current_date)

        for trip_name in trips:

            print(trips)

            num_clients[trip_name] = int(trips[trip_name])

            if trip_name == "Ticket to Ride - 09:30:00":

                if num_clients[trip_name] > 0:

                    num_guides[trip_name] = int((num_clients[trip_name] // 10)
                                            +(num_clients[trip_name] % 10 > 0))

                    num_drivers[trip_name] = int((num_clients[trip_name] // 20)
                                            +(num_clients[trip_name] % 20 > 0))

                    max_guides[
                        create_schedule.schedule_dictionaries.max_guides_trip_swictch[
                            trip_name
                        ]
                    ] = num_guides[trip_name]

                    max_drivers[
                        create_schedule.schedule_dictionaries.max_guides_trip_swictch[
                            trip_name
                        ]
                    ] = num_drivers[trip_name]

                    DialogBox = QtWidgets.QDialog()
                    ui_guides = popups.overnight_popup.Ui_overnight_popup()
                    ui_guides.setupUi(DialogBox, num_guides[trip_name],
                                        current_date,
                                        trip_role_assignment, DialogBox)
                    DialogBox.show()

                    print("shown")

                    if DialogBox.exec_():

                        print("exec")
                        trip_role_assignment = ui_guides.return_data()

                        print("trip role assignemt ",trip_role_assignment)

                else:

                    num_guides[trip_name] = 0
                    num_drivers[trip_name] = 0

            else:

                num_guides[trip_name] = int((num_clients[trip_name] // 10)
                                        +(num_clients[trip_name] % 10 > 0))

                num_drivers[trip_name] = int((num_clients[trip_name] // 20)
                                        +(num_clients[trip_name] % 20 > 0))

                print("tripname = ", trip_name)
                print("num_guides= ", num_guides[trip_name])
                print("num_drivers= ", num_drivers[trip_name])
                print("max= ", create_schedule.schedule_dictionaries.max_guides_trip_swictch[trip_name])

                if num_guides[trip_name] > max_guides[create_schedule.schedule_dictionaries.max_guides_trip_swictch[trip_name]]:

                    max_guides[
                        create_schedule.schedule_dictionaries.max_guides_trip_swictch[
                            trip_name
                        ]
                    ] = num_guides[trip_name]

                if num_drivers[trip_name] > max_drivers[create_schedule.schedule_dictionaries.max_guides_trip_swictch[trip_name]]:
                    max_drivers[
                        create_schedule.schedule_dictionaries.max_guides_trip_swictch[
                            trip_name
                        ]
                    ] = num_drivers[trip_name]

                print("\n")
                print("For: ", trip_name)
                print ("Number of Clients: ", num_clients[trip_name])
                print ("Number of Guides Needed: ", num_guides[trip_name])
                print ("Number of Drivers Needed: ", num_drivers[trip_name])

        total_guides_needed = 0
        total_drivers_needed = 0

        for x in num_guides:

            total_guides_needed += num_guides[x]

        for x in num_drivers:

            total_drivers_needed += num_drivers[x]

        if total_guides_needed > len(manage_staff.staff_util.get_total_guides()):

            DialogBox = QtWidgets.QDialog()
            ui_guides = popups.not_enough_guides_popup.Ui_not_enough_guides_popup()
            ui_guides.setupUi(DialogBox, DialogBox)
            DialogBox.show()

            print("shown")

            if DialogBox.exec_():
                print("exec")
                temp_guide = ui_guides.return_temp_guide()

                temp_guide_object = session_guide.query(manage_staff.guide.guide).filter(
                    manage_staff.guide.guide.name.in_(
                        [temp_guide])).update(
                            {'in_stream':'true'},synchronize_session=False
                        )

                session_guide.commit()

                print("Set to true : ", session_guide.query(manage_staff.guide.guide).filter(manage_staff.guide.guide.name.in_([temp_guide])))

        #if total_drivers_needed > len(manage_staff.staff_util.get_total_drivers()):
    #
    #        DialogBox = QtGui.QDialog()
    #        ui_guides = popups.not_enough_guides_popup.Ui_not_enough_guides_popup()
    #        ui_guides.setupUi(DialogBox, DialogBox)
    #        DialogBox.show()
    #
    #        print("shown")
    #
    #        if DialogBox.exec_():
    #            print("exec")
    #            temp_guide = ui_guides.return_temp_guide()
    #
    #            temp_guide_object = session_guide.query(manage_staff.guide.guide).filter(
    #                manage_staff.guide.guide.name.in_(
    #                    [temp_guide])).update(
    #                        {'in_stream':'true'},synchronize_session=False
    #                    )
    #
    #            session_guide.commit()
    #
    #            print("Set to true : ", session_guide.query(manage_staff.guide.guide).filter(manage_staff.guide.guide.name.in_([temp_guide])))

        for trip in create_schedule.schedule_dictionaries.trip_number_switch:

            if trip not in num_clients:

                num_clients[trip] = 0
                num_guides[trip] = 0
                num_drivers[trip] = 0

                print("\n")
                print("For: ", trip_name)
                print ("Number of Clients: ", num_clients)
                print ("Number of Guides Needed: ", num_guides)
                print ("Number of Drivers Needed: ", num_drivers)

        for trip in range(len(create_schedule.schedule_dictionaries.trip_types)):

            if trip != 4:

                print("max_guides: ", max_guides[trip])

                if (max_guides[trip] <= 4 and max_guides[trip] > 1 ):

                    for role_needed in range(max_guides[trip]):

                        print("Num guides needed", max_guides[trip], "for ", trip)

                        create_schedule_role(role_needed, current_date, trip_role_assignment, trip, class_IV_needed)


                elif(max_guides[trip] == 1):

                    create_schedule_role(0, current_date, trip_role_assignment, trip, class_IV_needed)
                    create_schedule_role(4, current_date, trip_role_assignment, trip, class_IV_needed)

                #class_IV_drivers = get_class_IV_drivers()
                #if total_drivers_needed <= class_IV_drivers:
                #print("max_drivers: ", max_drivers[trip])

                for role_needed in range(max_drivers[trip]):

                    print("Num drivers needed ", max_drivers[trip], "for ", trip)

                    create_schedule_role(role_needed+5, current_date, trip_role_assignment, trip, class_IV_needed)

        #print(trips)
        #print(num_guides)
        #print('trip role assignment: ', trip_role_assignment)
        print("CLASS IV NEEDED: ", class_IV_needed)

        copy_schedule_role(trips, trip_role_assignment, num_drivers, num_safety,
                            num_clients, num_guides,
                            max_guides, max_drivers, current_date_object, current_date)

        if temp_guide != 0:

            temp_guide_object = session_guide.query(manage_staff.guide.guide).filter(
                                    manage_staff.guide.guide.name.in_(
                                        [temp_guide])).update(
                                            {'in_stream':'false'},synchronize_session=False
                                        )

            session_guide.commit()

            print("returned to false: ", session_guide.query(manage_staff.guide.guide).filter(manage_staff.guide.guide.name.in_([temp_guide])))


            #if temp_driver != 0:
        #
        #        temp_guide_object = session_guide.query(manage_staff.guide.guide).filter(
        #                                manage_staff.guide.guide.name.in_(
        #                                    [temp_guide])).update(
        #                                        {'in_stream':'false'},synchronize_session=False
        #                                    )
        #
        #        session_guide.commit()
        #
        #        print("returned to false: ", session_guide.query(manage_staff.guide.guide).filter(manage_staff.guide.guide.name.in_([temp_guide])))


        #os.remove('trips_backup.db')
        #os.remove('staff_backup.db')

    #except:

        #print("ERROR OCCURRED")

        #copyfile('trips_backup.db', 'trips.db')
        #copyfile('staff_backup.db', 'staff.db')
        #os.remove('trips_backup.db')
        #os.remove('staff_backup.db')



################################################################################


def create_schedule_role(role, current_date, trip_role_assignment, trip, class_IV_needed):


    calculate_priority_list = get_priority.get_ordered_priority_list(trip, role, class_IV_needed)



    current_date_schedule = session_schedule.query(schedule).filter(
                                schedule.date == current_date
                            )

    #print("***", current_date_schedule)

    current_date_schedule_list = [u.__dict__ for u in current_date_schedule.all()]

    #print("***", current_date_schedule_list)
    #print('choosing ', role,' for ', trip)

    loop_controller = calculate_priority_list.copy()

    for candidate in loop_controller:

        #print('Candidate is: ', candidate)
        if candidate in trip_role_assignment.values():

            #print('Checking if ',candidate,' has been assigned but is not in db', trip_role_assignment)
            calculate_priority_list.remove(candidate)
            #print(calculate_priority_list)

    for trips in range(len(create_schedule.schedule_dictionaries.trip_switch_numerical)-1):
        #check database for candidate incase driver is guiding


        #print('Candidate is: ', candidate)

        for roles in range(len(create_schedule.schedule_dictionaries.role_switch)-1):

            #print('Candidate is: ', candidate)

            for candidate in loop_controller:

                staff_member = current_date_schedule_list[0][
                            create_schedule.schedule_dictionaries.role_switch[roles]
                            +create_schedule.schedule_dictionaries.trip_switch_numerical[trips]
                        ]
                #print('Checking if ',candidate,' is ', guide)

                if candidate is staff_member:

                    calculate_priority_list.remove(candidate)
                    #print('after removing ', candidate, ' ', calculate_priority_list,' is left')

    print(calculate_priority_list)

    if len(calculate_priority_list) > 0:

        trip_role_assignment[
            create_schedule.schedule_dictionaries.role_switch[role]
            +create_schedule.schedule_dictionaries.trip_types[trip]
        ] = calculate_priority_list[0]


        if role <= 4:
            candidate_object = session_guide.query(manage_staff.guide.guide).filter(
                                    manage_staff.guide.guide.name == calculate_priority_list[0]
                               )
            candidate_list = [u.__dict__ for u in candidate_object.all()]
            print("CANDIDATE IS GUIDE")

        else:
            candidate_object = session_driver.query(manage_staff.driver.driver).filter(
                                manage_staff.driver.driver.name == calculate_priority_list[0]
                               )

            candidate_list = [u.__dict__ for u in candidate_object.all()]
            print("CANDIDATE IS DRIVER");

        if  candidate_list[0]['has_class_IV'] == '1':
            print("HAS CLASS IV: ", candidate_list[0]['has_class_IV'])
            class_IV_needed[
                create_schedule.schedule_dictionaries.trip_types[trip]
            ] = 1;
            print("CLASS IV NEEDED: ", class_IV_needed)

        else:
            print("HAS CLASS IV: ", candidate_list[0]['has_class_IV'])
            if (create_schedule.schedule_dictionaries.trip_types[trip]
                    not in  class_IV_needed):
                print("NO ENTRY FOR THIS TRIP YET")
                class_IV_needed[
                    create_schedule.schedule_dictionaries.trip_types[trip]
                ] = 0;
                print("CLASS IV NEEDED: ", class_IV_needed)


    #else:
        #trip_role_assignment[create_schedule.schedule_dictionaries.role_switch[role]+create_schedule.schedule_dictionaries.trip_types[trip]] = "No Guides Left"
#schedule_update = session_schedule.query(schedule).update({create_schedule.schedule_dictionaries.role_switch[role]+create_schedule.schedule_dictionaries.trip_switch_numerical[trip]:calculated_priority_list[0]},synchronize_session=False)
#session_schedule.commit()



schedule_base.metadata.create_all(schedule_engine)

#excel_data = excel_scraper.scraper.excel_scraper('C:\\Users\\kayle\\Desktop\\Guide Schedule Software- All Versions\\Extra Gui Files\\Old Python Files\\data2.xlsx')
#current_date = '2018-08-13'
#create_schedule_day(excel_data, current_date)

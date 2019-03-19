
#def last_day_worked(staff_name, trip_name, current_date):
#
#    previous_date = calculate_previous_date(current_date)
#
#    for x in range (0,2):
#        c_trips.execute("SELECT trip_leader"+trip_switch_excel[trip_name]
#                        + " FROM ["+previous_date+"]")
#        guide = c_trips.fetchone()
#
#        if (staff_name == guide):
#            return previous_date
#        else:
#            previous_date = calculate_previous_date(previous_date)
#            x+=1
#    return ""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

from sqlalchemy.orm import load_only

import create_schedule

import manage_staff
from manage_staff import guide
from manage_staff import driver

session_guide = guide.guide_session()
session_driver = driver.driver_session()

################################################################################

def is_day_off(guide_name, current_date):

    days_since = 0
    previous_date = calculate_previous_date(current_date)

    for x in range(0,6):
        for y in range(0,6):
            c_trips.execute("SELECT " +role_switch[x]+trip_switch_numerical[y] +
                            " FROM ["+current_date+"]")
            guide = c_trips.fetchone()

            if(guide_name  == guide):
                days_since+=1
                previous_date = calculate_previous_date(previous_date)
                return days_since
            else:
                y+=1
        x+=1
    return days_since

################################################################################


def update_num_trips_guide(guide_name, trip_name, priority_change, role):

    if guide_name != 'No Guides Left':
        num_trips_object = session_guide.query(manage_staff.guide.guide).filter(
                            manage_staff.guide.guide.name.in_(
                            [guide_name])).options(load_only(
                                create_schedule.schedule_dictionaries.guide_roles[role]
                                +create_schedule.schedule_dictionaries.time_types[0]
                                +create_schedule.schedule_dictionaries.trip_types[trip_name]
                            ))
        num_trips_list = [u.__dict__ for u in num_trips_object.all()]
        num_trips = num_trips_list[0][create_schedule.schedule_dictionaries.guide_roles[role]
                                      +create_schedule.schedule_dictionaries.time_types[0]
                                      +create_schedule.schedule_dictionaries.trip_types[trip_name]]

        num_trips_object = session_guide.query(manage_staff.guide.guide).filter(
                            manage_staff.guide.guide.name.in_(
                            [guide_name])).update(
                                {create_schedule.schedule_dictionaries.guide_roles[role]
                                +create_schedule.schedule_dictionaries.time_types[0]
                                +create_schedule.schedule_dictionaries.trip_types[trip_name]:num_trips
                                +priority_change},synchronize_session=False)
        session_guide.commit()

        num_trips_object = session_guide.query(manage_staff.guide.guide).filter(
                            manage_staff.guide.guide.name.in_(
                            [guide_name])).options(load_only(
                                create_schedule.schedule_dictionaries.guide_roles[role]
                                +create_schedule.schedule_dictionaries.time_types[1]
                                +create_schedule.schedule_dictionaries.trip_types[trip_name]))

        num_trips_list = [u.__dict__ for u in num_trips_object.all()]

        num_trips = num_trips_list[0][create_schedule.schedule_dictionaries.guide_roles[role]
                    +create_schedule.schedule_dictionaries.time_types[1]
                    +create_schedule.schedule_dictionaries.trip_types[trip_name]]

        num_trips_object = session_guide.query(manage_staff.guide.guide).filter(
                            manage_staff.guide.guide.name.in_([guide_name])).update(
                                {create_schedule.schedule_dictionaries.guide_roles[role]
                                +create_schedule.schedule_dictionaries.time_types[1]
                                +create_schedule.schedule_dictionaries.trip_types[trip_name]:num_trips
                                +priority_change},synchronize_session=False)

        session_guide.commit()

################################################################################


def update_num_trips_driver(driver_name, trip_name, priority_change):

    num_trips_object = session_driver.query(manage_staff.driver.driver).filter(
                            manage_staff.driver.driver.name.in_([driver_name])).options(
                                load_only(
                                    "driven_"
                                    +create_schedule.schedule_dictionaries.time_types[0]
                                    +create_schedule.schedule_dictionaries.trip_types[trip_name]
                                )
                            )

    num_trips_list = [u.__dict__ for u in num_trips_object.all()]

    num_trips = num_trips_list[0]["driven_"
                                  +create_schedule.schedule_dictionaries.time_types[0]
                                  +create_schedule.schedule_dictionaries.trip_types[trip_name]]

    num_trips_object = session_driver.query(manage_staff.driver.driver).filter(
                        manage_staff.driver.driver.name.in_([driver_name])).update(
                            {"driven_"
                            +create_schedule.schedule_dictionaries.time_types[0]
                            +create_schedule.schedule_dictionaries.trip_types[trip_name]:num_trips
                            +priority_change},synchronize_session=False)

    session_driver.commit()

    num_trips_object = session_driver.query(manage_staff.driver.driver).filter(
                            manage_staff.driver.driver.name.in_([driver_name])).options(
                                load_only("driven_"
                                    +create_schedule.schedule_dictionaries.time_types[1]
                                    +create_schedule.schedule_dictionaries.trip_types[trip_name]
                                )
                            )

    num_trips_list = [u.__dict__ for u in num_trips_object.all()]

    num_trips = num_trips_list[0]["driven_"
                                  +create_schedule.schedule_dictionaries.time_types[1]
                                  +create_schedule.schedule_dictionaries.trip_types[trip_name]]

    num_trips_object = session_driver.query(manage_staff.driver.driver).filter(
                        manage_staff.driver.driver.name.in_([driver_name])).update(
                            {"driven_"
                            +create_schedule.schedule_dictionaries.time_types[1]
                            +create_schedule.schedule_dictionaries.trip_types[trip_name]:num_trips
                            +priority_change},synchronize_session=False)

    session_driver.commit()

################################################################################


def get_total_guides():

    all_guides_object = session_guide.query(manage_staff.guide.guide).filter(
                            manage_staff.guide.guide.in_stream.in_(['true']))

    all_guides_list = [u.__dict__ for u in all_guides_object.all()]

    return all_guides_list

################################################################################


def get_total_temp_guides():

    temp_guides_object = session_guide.query(manage_staff.guide.guide).filter(
                            manage_staff.guide.guide.in_stream.in_(['false']))

    temp_guides_list = [u.__dict__ for u in temp_guides_object.all()]

    return temp_guides_list

################################################################################

def get_total_drivers():

    all_drivers_object = session_guide.query(manage_staff.driver.driver).filter(
                            manage_staff.driver.driver.in_stream.in_(['true']))

    all_drivers_list = [u.__dict__ for u in all_drivers_object.all()]

    return all_drivers_list

################################################################################


def get_total_temp_drivers():

    temp_drivers_object = session_guide.query(manage_staff.driver.driver).filter(
                            manage_staff.driver.driver.in_stream.in_(['false']))

    temp_drivers_list = [u.__dict__ for u in temp_drivers_object.all()]

    return temp_drivers_list

################################################################################


def get_guides_can_work(trip_type, role_type):

    guides_can_work_object = session_guide.query(manage_staff.guide.guide).filter(
                                manage_staff.guide.guide.in_stream.in_(['true']))

    guides_can_work_list = [u.__dict__ for u in guides_can_work_object.all()]

    final_guides_list = []

    for n in range(len(guides_can_work_list)):

        print("for loop entered")
        print("guide: ", guides_can_work_list[n]['name'] ,", " , guides_can_work_list[n][create_schedule.schedule_dictionaries.guide_roles[role_type]+create_schedule.schedule_dictionaries.trip_types[trip_type]])

        if guides_can_work_list[n][create_schedule.schedule_dictionaries.guide_roles[role_type]
                +create_schedule.schedule_dictionaries.trip_types[trip_type]] == '1':

            final_guides_list.append(guides_can_work_list[n]['name'])

            print(final_guides_list)
    return final_guides_list

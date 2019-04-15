from sqlalchemy.sql.expression import func

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
from create_schedule import create_new_schedule

import manage_staff
from manage_staff import guide
from manage_staff import driver

#TODO: Update so uses SQLAlchemy
def is_day_off(guide_name, current_date):
    """Determines whether or not a guide is working on a given day

    Parameters
    ----------
    guide_name: str
        A string representing the name of the guide to be considered
    current_date : str
        A string representing the day to be checked formatted YYYY-MM-DD

    Method Calls
    ------------
        -calculate_previous_date()

    Returns
    ------
    int
        An integer representing the number of days since a guide has had a day
        where they did not work
    """

    days_since = 0
    previous_date = calculate_previous_date(current_date)

    for x in range(0,6):
        for y in range(0,6):
            c_trips.execute("SELECT " +role_switch[x]+trip_switch_numerical[y] +
                            " FROM ["+current_date+"]")
            guide = c_trips.fetchone()

            if(guide_name == guide):
                days_since+=1
                previous_date = calculate_previous_date(previous_date)
                return days_since
            else:
                y+=1
        x+=1
    return days_since

def update_num_trips_guide(session_guide, session_schedule, guide_name,
                            trip_name, priority_change,
                            role, date_to_be_updated):
    """Updates the number of times a guide has worked a given trip

    Parameters
    ----------
    session_guide: session
        A session object that allows access to the guide table in staff.db
    session_schedule: session
        A session object that allows access to the schedule table in trips.db
    guide_name: str
        A string representing the name of the guide to be updated
    trip_name: int
        An integer value taken from the max_guides_trip_swictch dictionary
        representing a value in the trip_types dictionary
    role: int
        An integer representing the number to be added to the current value
    date_to_be_updated: str???
        A string representation of the date where the update occurs formatted
        YYYY-MM-DD???

    Method Calls
    ------------
        -get_current_period()
    """

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

        period_to_be_updated = create_schedule.schedule_util.get_current_period(date_to_be_updated)
        print("PERIOD TO BE UPDATED FOR ",role, ": ", period_to_be_updated)
        period_object = session_schedule.query(create_schedule.create_new_schedule.schedule).options(
                            load_only('period')
                        )

        period_list = [u.__dict__ for u in period_object.all()]
        period_max = 0
        for period in period_list:
            if period['period'] > period_max:
                period_max = period['period']

        print("PERIOD CURRENTLY BEING RECORDED: ", period_max)
        if period_to_be_updated == period_max:

            print("PERIOD'S MATCHED, WILL BE UPDATING FOR", role,": ",period_to_be_updated)

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

def update_num_trips_driver(session_driver, session_schedule, driver_name,
                            trip_name, priority_change, date_to_be_updated):
    """Updates the number of times a driver has worked a given trip

    Parameters
    ----------
    session_driver: session
        A session object that allows access to the driver table in staff.db
    session_schedule: session
        A session object that allows access to the schedule table in trips.db
    guide_name: str
        A string representing the name of the guide to be updated
    trip_name: int
        An integer value taken from the max_guides_trip_swictch dictionary
        representing a value in the trip_types dictionary
    role: int
        An integer representing the number to be added to the current value
    date_to_be_updated: str???
        A string representation of the date where the update occurs formatted
        YYYY-MM-DD???

    Method Calls
    ------------
        -get_current_period()
    """

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

    period_to_be_updated = create_schedule.schedule_util.get_current_period(date_to_be_updated)
    print("PERIOD TO BE UPDATED FOR DRIVER: ", period_to_be_updated)
    period_object = session_schedule.query(create_schedule.create_new_schedule.schedule).options(
                        load_only('period')
                    )
    period_list = [u.__dict__ for u in period_object.all()]

    period_max = 0
    for period in period_list:
        if period['period'] > period_max:
            period_max = period['period']

    print("PERIOD CURRENTLY BEING RECORDED FOR DRIVER: ", period_max)
    if period_to_be_updated == period_max:

        print("PERIOD'S MATCHED, WILL BE UPDATING FOR DRIVER: ",period_to_be_updated)

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

def reset_this_period(session_guide, session_driver):
    """Sets the number of times a trip is worked in the current period to the
    default value

    Parameters
    ----------
    session_guide: session
        A session object that allows access to the guide table in staff.db
    session_driver: session
        A session object that allows access to the schedule table in trips.db

    Method Calls
    ------------
        -get_total_guides()
        -get_total_drivers()
    """

    all_drivers = get_total_drivers(session_driver)
    all_guides = get_total_guides(session_guide)

    for driver in all_drivers:
        name = driver['name']
        for trip in create_schedule.schedule_dictionaries.trip_types:
            num_trips_object = session_driver.query(manage_staff.driver.driver).filter(
                                manage_staff.driver.driver.name == name).update(
                                    {"driven_"
                                    +create_schedule.schedule_dictionaries.time_types[1]
                                    +create_schedule.schedule_dictionaries.trip_types[trip]:0
                                    },synchronize_session=False)

            session_driver.commit()


    for guide in all_guides:
        name = guide['name']
        for trip in create_schedule.schedule_dictionaries.trip_types:
            for role in create_schedule.schedule_dictionaries.guide_roles:
                num_trips_object = session_guide.query(manage_staff.guide.guide).filter(
                                    manage_staff.guide.guide.name ==name).update(
                                        {create_schedule.schedule_dictionaries.guide_roles[role]
                                        +create_schedule.schedule_dictionaries.time_types[1]
                                        +create_schedule.schedule_dictionaries.trip_types[trip]:0
                                        },synchronize_session=False)

                session_guide.commit()

def get_total_guides(session_guide):
    """Creates a list of all of the guides currently stored in the guide table

    Parameters
    ----------
    session_guide: session
        A session object that allows access to the guide table in staff.db

    Returns
    -------
    list
        a list of dictionaries containing all of the information on each guide
        that is stored in the database
    """

    all_guides_object = session_guide.query(manage_staff.guide.guide).filter(
                            manage_staff.guide.guide.in_stream.in_(['true']))

    all_guides_list = [u.__dict__ for u in all_guides_object.all()]

    return all_guides_list

def get_total_temp_guides(session_guide):
    """Creates a list of all of the guides currently stored in the guides table
    that are not in the stream

    Parameters
    ----------
    session_guide: session
        A session object that allows access to the guide table in staff.db

    Returns
    -------
    list
        a list of dictionaries containing all of the information on each guide
        that is stored in the database
    """

    temp_guides_object = session_guide.query(manage_staff.guide.guide).filter(
                            manage_staff.guide.guide.in_stream.in_(['false']))

    temp_guides_list = [u.__dict__ for u in temp_guides_object.all()]

    return temp_guides_list

def get_total_drivers(session_driver):
    """Creates a list of all of the drivers currently stored in the driver table

    Parameters
    ----------
    session_driver: session
        A session object that allows access to the driver table in staff.db

    Returns
    -------
    list
        a list of dictionaries containing all of the information on each driver
        that is stored in the database
    """

    all_drivers_object = session_driver.query(manage_staff.driver.driver).filter(
                            manage_staff.driver.driver.in_stream.in_(['true']))

    all_drivers_list = [u.__dict__ for u in all_drivers_object.all()]
    return all_drivers_list

def get_total_temp_drivers():
    """Creates a list of all of the drivers currently stored in the driver table
    that are not in the stream

    Parameters
    ----------
    session_driver: session
        A session object that allows access to the driver table in staff.db

    Returns
    -------
    list
        a list of dictionaries containing all of the information stored in the
        database on each driver
    """

    temp_drivers_object = session_guide.query(manage_staff.driver.driver).filter(
                            manage_staff.driver.driver.in_stream.in_(['false']))

    temp_drivers_list = [u.__dict__ for u in temp_drivers_object.all()]

    return temp_drivers_list

def get_guides_can_work(session_guide, trip_type, role_type):
    """Creates a list of all of the guides currently stored in the guides table
    that can perform the given role for the given trip type

    Parameters
    ----------
    session_guide: session
        A session object that allows access to the guide table in staff.db
    trip_type: int
        An integer value representing a type of trip that can be used as a key
        in the trip_types dictionary
    role_type: int
        An integer value representing a type of role that can be used as a key
        in the guide_roles dictionary

    Returns
    -------
    list
        a list of dictionaries containing all of the information stored in the
        database on each guide who is able to perform the role for the trip type
    """

    guides_can_work_object = session_guide.query(manage_staff.guide.guide).filter(
                                manage_staff.guide.guide.in_stream.in_(['true']))

    guides_can_work_list = [u.__dict__ for u in guides_can_work_object.all()]

    final_guides_list = []

    for n in enumerate(guides_can_work_list):
        if guides_can_work_list[n][create_schedule.schedule_dictionaries.guide_roles[role_type]
                +create_schedule.schedule_dictionaries.trip_types[trip_type]] == '1':
            final_guides_list.append(guides_can_work_list[n]['name'])

    return final_guides_list

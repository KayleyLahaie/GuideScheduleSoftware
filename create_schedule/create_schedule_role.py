import create_schedule
from create_schedule import create_new_schedule
from create_schedule import get_priority

import manage_staff
from manage_staff import guide
from manage_staff import driver

session_schedule = create_new_schedule.schedule_session()
session_guide = guide.guide_session()
session_driver = driver.driver_session()


def create_schedule_role(role, current_date, trip_role_assignment, trip,
                            class_IV_needed, trips_needing_class_IV_guide):
    """Create the schedule for all trips for the given day

    Parameters
    ----------
    role: int
        A number representing the role being assigned where role corresponds to
        the key values of the role_switch dictionary
    current_date : date
        A date object representing the date for which a schedule must be
        created
    trip_role_assignment: dict
        An empty dictionary to be filled with the names of the staff members
        assigned to each role
    trip: int
        An integer value representing the trip being scheduled where trip
        corresponds to the key values of the trip_types dictionary
    class_IV_needed: dict
        An empty dictionary used to keep track of which trips need a guide with
        a Class IV driver's license
    trips_needing_class_IV_guide: int
        An integer representing the number of trips that will need a guide with
        a Class IV drivers license after all drivers with licenses have been
        assigned

    Method Calls
    ------------
        -get_ordered_priority_list()
        -calculate_priority_class_IV()

    Returns
    -------
    int
        An integer representing the number of trips that will need a guide with
        a Class IV drivers license after all drivers with licenses have been
        assigned
    """

    calculate_priority_list = get_priority.get_ordered_priority_list(
                                session_guide, session_driver,
                                trip, role, class_IV_needed,
                                trips_needing_class_IV_guide
                            )
    class_IV_candidate_object = session_guide.query(manage_staff.guide.guide).filter(
                            manage_staff.guide.guide.has_class_IV == '1'
                       )
    class_IV_candidate_list = [u.__dict__ for u in class_IV_candidate_object.all()]

    print("NUMBER OF TRIPS NEEDING CLASS IV GUIDE IS: ", trips_needing_class_IV_guide)
    print("ROLE BEING SCHEDULED IS: ", role)

    if role <= 4:
        if trips_needing_class_IV_guide > 0:

            print("TRIP ROLE ASSIGNMENT: ", trip_role_assignment)

            staff = []
            class_IV = 0

            print("CANDIDATE LIST- CREATE SCHEDULE ROLE: ", class_IV_candidate_list)

            for role_staff in create_schedule.schedule_dictionaries.role_switch:
                if (create_schedule.schedule_dictionaries.role_switch[role_staff]
                        +create_schedule.schedule_dictionaries.trip_types[trip]
                        in trip_role_assignment):
                    staff.append(trip_role_assignment[
                            create_schedule.schedule_dictionaries.role_switch[role_staff]
                            +create_schedule.schedule_dictionaries.trip_types[trip]
                            ])

            if staff:
                for guide in staff:

                    print("GUIDE: ", guide)

                    for candiate in class_IV_candidate_list:
                        if guide == candiate['name']:

                            print(guide," == ", candiate['name'])

                            class_IV = 1

            if class_IV == 1:
                calculate_priority_list = get_priority.calculate_priority_class_IV(calculate_priority_list)

    loop_controller = calculate_priority_list.copy()

    current_date_schedule = session_schedule.query(create_new_schedule.schedule).filter(
                                create_new_schedule.schedule.date == current_date
                            )
    current_date_schedule_list = [u.__dict__ for u in current_date_schedule.all()]


    for candidate in loop_controller:
        if candidate in trip_role_assignment.values():
            calculate_priority_list.remove(candidate)


    for trips in range(len(create_schedule.schedule_dictionaries.trip_switch_numerical)-1):
        for roles in range(len(create_schedule.schedule_dictionaries.role_switch)-1):
            for candidate in loop_controller:
                staff_member = current_date_schedule_list[0][
                            create_schedule.schedule_dictionaries.role_switch[roles]
                            +create_schedule.schedule_dictionaries.trip_switch_numerical[trips]
                        ]
                if candidate is staff_member:
                    calculate_priority_list.remove(candidate)


    if len(calculate_priority_list) > 0:

        trip_role_assignment[
            create_schedule.schedule_dictionaries.role_switch[role]
            +create_schedule.schedule_dictionaries.trip_types[trip]
        ] = calculate_priority_list[0]

        for candidate in class_IV_candidate_list:
            if calculate_priority_list[0] == candidate['name']:
                trips_needing_class_IV_guide -=1

        print("STAFF MEMBER SELECTED: ", calculate_priority_list[0])

        if role <= 4:

            print("CANDIDATE IS GUIDE")
            candidate_object = session_guide.query(manage_staff.guide.guide).filter(
                                    manage_staff.guide.guide.name == calculate_priority_list[0]
                               )

            candidate_list = [u.__dict__ for u in candidate_object.all()]


        else:
            candidate_object = session_driver.query(manage_staff.driver.driver).filter(
                                manage_staff.driver.driver.name == calculate_priority_list[0]
                               )
            candidate_list = [u.__dict__ for u in candidate_object.all()]

            print("CANDIDATE IS DRIVER");

        if  candidate_list[0]['has_class_IV'] == '1':

            print("DOES HAVE CLASS IV: "+candidate_list[0]['name'])

            class_IV_needed[
                create_schedule.schedule_dictionaries.trip_types[trip]
            ] = 1;

        else:

            print("DOES NOT HAVE CLASS IV: "+candidate_list[0]['name'])

            if (create_schedule.schedule_dictionaries.trip_types[trip]
                    not in  class_IV_needed):
                class_IV_needed[
                    create_schedule.schedule_dictionaries.trip_types[trip]
                ] = 0;

    return trips_needing_class_IV_guide

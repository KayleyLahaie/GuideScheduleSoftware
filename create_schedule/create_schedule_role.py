import create_schedule
from create_schedule import create_new_schedule
from create_schedule import get_priority

import manage_staff
from manage_staff import guide
from manage_staff import driver

session_schedule = create_new_schedule.schedule_session()
session_guide = guide.guide_session()
session_driver = driver.driver_session()


def create_schedule_role(role, current_date, trip_role_assignment, trip, class_IV_needed, trips_needing_class_IV_guide):

    calculate_priority_list = get_priority.get_ordered_priority_list(
                                trip, role, class_IV_needed,
                                trips_needing_class_IV_guide
                            )

    class_IV_candidate_object = session_guide.query(manage_staff.guide.guide).filter(
                            manage_staff.guide.guide.has_class_IV == '1'
                       )

    class_IV_candidate_list = [u.__dict__ for u in class_IV_candidate_object.all()]
    print("TRIPS NEEDING CLASS IV GUIDE IS: ", trips_needing_class_IV_guide)
    print("ROLE IS: ", role)
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

    #print("***", current_date_schedule_list)
    #print('choosing ', role,' for ', trip)

    loop_controller = calculate_priority_list.copy()

    current_date_schedule = session_schedule.query(create_new_schedule.schedule).filter(
                                create_new_schedule.schedule.date == current_date
                            )

    current_date_schedule_list = [u.__dict__ for u in current_date_schedule.all()]


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

        for candidate in class_IV_candidate_list:
            if calculate_priority_list[0] == candidate['name']:
                trips_needing_class_IV_guide -=1

        print("GUIDE SELECTED: ", calculate_priority_list[0])
        print(role)
        if role <= 4:
            print("CANDIDATE IS GUIDE")
            candidate_object = session_guide.query(manage_staff.guide.guide).filter(
                                    manage_staff.guide.guide.name == calculate_priority_list[0]
                               )
            print(candidate_object)
            candidate_list = [u.__dict__ for u in candidate_object.all()]
            print(candidate_list)

        else:
            candidate_object = session_driver.query(manage_staff.driver.driver).filter(
                                manage_staff.driver.driver.name == calculate_priority_list[0]
                               )

            candidate_list = [u.__dict__ for u in candidate_object.all()]
            print("CANDIDATE IS DRIVER");

        if  candidate_list[0]['has_class_IV'] == '1':
            #print("HAS CLASS IV: ", candidate_list[0]['has_class_IV'])
            class_IV_needed[
                create_schedule.schedule_dictionaries.trip_types[trip]
            ] = 1;
            #print("CLASS IV NEEDED: ", class_IV_needed)

        else:
            #print("HAS CLASS IV: ", candidate_list[0]['has_class_IV'])
            if (create_schedule.schedule_dictionaries.trip_types[trip]
                    not in  class_IV_needed):
                #print("NO ENTRY FOR THIS TRIP YET")
                class_IV_needed[
                    create_schedule.schedule_dictionaries.trip_types[trip]
                ] = 0;
                #print("CLASS IV NEEDED: ", class_IV_needed)

    return trips_needing_class_IV_guide
    #else:
        #trip_role_assignment[create_schedule.schedule_dictionaries.role_switch[role]+create_schedule.schedule_dictionaries.trip_types[trip]] = "No Guides Left"
#schedule_update = session_schedule.query(schedule).update({create_schedule.schedule_dictionaries.role_switch[role]+create_schedule.schedule_dictionaries.trip_switch_numerical[trip]:calculated_priority_list[0]},synchronize_session=False)
#session_schedule.commit()

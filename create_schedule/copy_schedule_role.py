import create_schedule
from create_schedule import create_new_schedule

import manage_staff
from manage_staff import staff_util

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
                                1, create_schedule.schedule_dictionaries.role_update_switch[role],
                                current_date
                            )

                        else:
                            manage_staff.staff_util.update_num_trips_driver(
                                trip_role_assignment[
                                    create_schedule.schedule_dictionaries.role_switch[role]
                                    +create_schedule.schedule_dictionaries.trip_types[
                                        create_schedule.schedule_dictionaries.max_guides_trip_swictch[trip_name]]],
                                create_schedule.schedule_dictionaries.max_guides_trip_swictch[trip_name],
                                1, current_date
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
                            create_schedule.schedule_dictionaries.role_update_switch[role],
                            current_date
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
                        create_schedule.schedule_dictionaries.role_update_switch[0],
                        current_date
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
                            create_schedule.schedule_dictionaries.role_update_switch[4],
                            current_date
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
                                create_schedule.schedule_dictionaries.role_update_switch[4],
                                current_date
                            )

    print(trip_role_assignment_final)

    create_schedule.create_new_schedule.submit_to_database(trip_role_assignment_final, num_drivers, num_clients,
                        num_guides, num_safety,
                        current_date_object, current_date)

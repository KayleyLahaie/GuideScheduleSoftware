import sqlite3
import collections
import create_schedule
import manage_staff
import operator

from create_schedule import schedule_dictionaries

connection_staff = sqlite3.connect('staff.db')
c_staff = connection_staff.cursor()

session_guide = manage_staff.guide.guide_session()
session_driver = manage_staff.driver.driver_session()

################################################################################

def get_guide_priority_matrix():

    guide_dict = {}

    guide_object = session_guide.query(manage_staff.guide.guide)

    guide_list = [u.__dict__ for u in guide_object.all()]


    for num_guides in range(len(guide_list)):
        if guide_list[num_guides]['in_stream'] == 'true':
            guide_name = guide_list[num_guides]['name']
            current_guide_priorities = []

            #x/y
            role_held_quotient = []


            #a/b
            trip_worked_quotient = []


            #sum(g(i)w(i))
            sum_weights = 0
            #g(i)
            g_of_i = []


            for x in range(len(create_schedule.schedule_dictionaries.trip_types)):
                for y in range(len(create_schedule.schedule_dictionaries.guide_roles)):

                    #x
                    times_role_held= []
                    #y
                    total_times_role_held = []
                    #a
                    times_trip_worked = []
                    #b
                    total_times_trip_worked = []
                    for z in range(len(create_schedule.schedule_dictionaries.time_types)):

                        #print(create_schedule.schedule_dictionaries.guide_roles[y]+create_schedule.schedule_dictionaries.time_types[z]+create_schedule.schedule_dictionaries.trip_types[x])

                        times_role_held.append(
                            guide_list[num_guides][create_schedule.schedule_dictionaries.guide_roles[y]
                            +create_schedule.schedule_dictionaries.time_types[z]
                            +create_schedule.schedule_dictionaries.trip_types[x]]
                        )

                        #print(guide_name, ' has held role ', create_schedule.schedule_dictionaries.guide_roles[y],
                        #      ' for trip ',create_schedule.schedule_dictionaries.trip_types[x],
                        #      ' during ',create_schedule.schedule_dictionaries.time_types[z], times_role_held[z], 'times' )

                        total_times_role_held.append(0)
                        total_times_trip_worked.append(0)

                        for guides in range(len(guide_list)):

                            total_times_role_held[z] += guide_list[guides][create_schedule.schedule_dictionaries.guide_roles[y]
                                                        +create_schedule.schedule_dictionaries.time_types[z]
                                                        +create_schedule.schedule_dictionaries.trip_types[x]]

                            for num_roles in range(len(create_schedule.schedule_dictionaries.guide_roles)):

                                total_times_trip_worked[z] += guide_list[guides][create_schedule.schedule_dictionaries.guide_roles[num_roles]
                                                                +create_schedule.schedule_dictionaries.time_types[z]
                                                                +create_schedule.schedule_dictionaries.trip_types[x]]

                        #print('the total number of times role ', create_schedule.schedule_dictionaries.guide_roles[y],
                        #      ' for trip ',create_schedule.schedule_dictionaries.trip_types[x],
                        #      ' during ',create_schedule.schedule_dictionaries.time_types[z], 'has been held is ', total_times_role_held[z])

                        if(total_times_role_held[z] != 0):

                            role_held_quotient.append(times_role_held[z] / total_times_role_held[z])

                        else:

                            role_held_quotient.append(1)

                        #print('role held quotient for', create_schedule.schedule_dictionaries.guide_roles[y],
                        #      ' for trip ',create_schedule.schedule_dictionaries.trip_types[x],
                        #      ' during ',create_schedule.schedule_dictionaries.time_types[z], ' is ', role_held_quotient[z])

                        times_trip_worked.append(0)
                        for num_roles in range(len(create_schedule.schedule_dictionaries.guide_roles)):

                            times_trip_worked[z] += guide_list[num_guides][create_schedule.schedule_dictionaries.guide_roles[num_roles]
                                                    +create_schedule.schedule_dictionaries.time_types[z]

                            +create_schedule.schedule_dictionaries.trip_types[x]]

                        #print(guide_name, ' worked ', create_schedule.schedule_dictionaries.trip_types[x],' ', times_trip_worked[z], 'times')
                        #print(' all guides worked ', create_schedule.schedule_dictionaries.trip_types[x],' ', total_times_trip_worked[z], 'times')

                        if (total_times_trip_worked[z] != 0):

                            trip_worked_quotient.append(times_trip_worked[z]/total_times_trip_worked[z])

                        else:

                            trip_worked_quotient.append(1)

                        #print('trip worked quotient for trip ', create_schedule.schedule_dictionaries.trip_types[x],
                             # ' during ',create_schedule.schedule_dictionaries.time_types[z], ' is ', trip_worked_quotient[z])

                    if guide_list[num_guides][create_schedule.schedule_dictionaries.guide_roles_2[y]
                            +create_schedule.schedule_dictionaries.trip_types[x]] == '1':

                        g_of_i.append(1)

                    else:

                        g_of_i.append(0)

                    #print(guide_name, 'can ', create_schedule.schedule_dictionaries.guide_roles_2[y], ' (y/n): ',g_of_i[y])

                sum_weights += (0.5)*float(g_of_i[y])*create_schedule.schedule_dictionaries.trip_weight[x]

                #print('sum_weights: ', sum_weights)
                #print('role_held_quotient:', role_held_quotient)
                #print('trip_worked_quotient: ', trip_worked_quotient)
                #print('g(i): ', g_of_i)

            sum_weights += 0.5

            x = 0

            for i in range(0,30,2):

                if(g_of_i[x] == 0):
                    current_guide_priorities.append(1);
                else:
                    current_guide_priorities.append(
                                                role_held_quotient[i]
                                                *trip_worked_quotient[i]
                                                *sum_weights
                                                *g_of_i[x]
                                             )

                x+=1

                #print('current guide priorities: ', i ,' ', current_guide_priorities)

            guide_dict[guide_name] = current_guide_priorities

    for guide in range(len(guide_list)):

        guide_name = guide_list[guide]['name']

        #print(guide_name, ': ',guide_dict[guide_name][6])

    return guide_dict

################################################################################
# trip and role =  numbers from schedule_dictionaries.trip_type and schedule_dictionaries.guide_roles
def get_ordered_priority_list(trip, role):

    if role <= 4:

        print("creating guide schedule for role: ", role)

        guide_priority_matrix = get_guide_priority_matrix()

        #print("guides: ",guide_priority_matrix)
        print('\n\n',trip,role,': ')

        guides = {}
        guides_ordered_name = []
        guides_ordered_priority = []

        for key in guide_priority_matrix:

            #print("role", schedule_dictionaries.guide_roles_converter[role])
            #print("trip", trip)
            #print("3*trip", 3*trip)
            #print("role+(3*trip)", schedule_dictionaries.guide_roles_converter[role]+(3*trip))

            guides[key] = guide_priority_matrix[key][
                            schedule_dictionaries.guide_roles_converter[role]
                            +(3*trip)]

        #print('All Guides: ', guides)

        for num_guides in range(len(guides)):

            max_guide = max(guides.items(), key=operator.itemgetter(1))[0]

            guides_ordered_name.append(max_guide)

            guides_ordered_priority.append(guides[max_guide])

            del guides[max_guide]

        #print('Guides (ordered): ', guides_ordered_name)
        guides_ordered_name = list(reversed(guides_ordered_name))
        guides_ordered_priority = list(reversed(guides_ordered_priority))
        #print('Guides (reversed): ', guides_ordered_name)
        #print('Guides (reversed): ', guides_ordered_priority)

        for number in guides_ordered_priority:

            if number == 0.0:

                i = guides_ordered_priority.index(number)

                del guides_ordered_priority[i]
                del guides_ordered_name[i]

        #calculated_priority_guides = calculate_priority(guide_priority_matrix, guides_ordered_name, guides_ordered_priority, trip, role)
        return guides_ordered_name

    else:

        print("creating driver schedule for role: ", role)

        driver_priority_matrix = get_driver_priority_matrix()

        #print("guides: ",guide_priority_matrix)
        #print('\n\n',trip,role,': ')

        drivers = {}
        drivers_ordered_name = []
        drivers_ordered_priority = []

        for key in driver_priority_matrix:

            #print("role", schedule_dictionaries.guide_roles_converter[role])
            #print("trip", trip)
            #print("3*trip", 3*trip)
            #print("role+(3*trip)", schedule_dictionaries.guide_roles_converter[role]+(3*trip))

            print("role+(trip): ", role+(2*trip))
            print(role)
            print(trip)
            print(len(driver_priority_matrix[key]))

            drivers[key] = driver_priority_matrix[key][
                            trip]

        #print('All Guides: ', guides)

        for num_drivers in range(len(drivers)):

            max_driver = max(drivers.items(), key=operator.itemgetter(1))[0]

            drivers_ordered_name.append(max_driver)

            drivers_ordered_priority.append(drivers[max_driver])

            del drivers[max_driver]

        #print('Guides (ordered): ', guides_ordered_name)
        drivers_ordered_name = list(reversed(drivers_ordered_name))
        drivers_ordered_priority = list(reversed(drivers_ordered_priority))
        #print('Guides (reversed): ', guides_ordered_name)
        #print('Guides (reversed): ', guides_ordered_priority)

        for number in drivers_ordered_priority:

            if number == 0:

                i = drivers_ordered_priority.index(number)

                del drivers_ordered_priority[i]
                del drivers_ordered_name[i]

        #calculated_priority_guides = calculate_priority(guide_priority_matrix, guides_ordered_name, guides_ordered_priority, trip, role)
        return drivers_ordered_name

################################################################################

def calculate_priority(guide_priority_matrix, guides_ordered_name, guides_ordered_priority, trip, role):

    priority_difference=[]
    calculated_priority_guides=[]

    for guides in range(len(guides_ordered_name)):

        guide_top_priority = min(guide_priority_matrix[guides_ordered_name[guides]])
        #print(guides_ordered_name[guides],'\'s priority for ', role, trip,': ', guides_ordered_priority[guides])
        #print(guides_ordered_name[guides],'\'s top priority ', role, trip,': ', guide_top_priority)
        difference = guides_ordered_priority[guides] - guide_top_priority

        if difference >= guide_top_priority:

            priority_difference.append(guides_ordered_priority[guides] - guide_top_priority)
            #print('Priority Differece: ', priority_difference[guides])

        else:

            priority_difference.append(1)
    #print('Priority Difference: ', priority_difference)

    for guides in range(len(guides_ordered_name)):

        max_difference = max(priority_difference)
        highest_priority_guide = guides_ordered_name[priority_difference.index(max_difference)]
        calculated_priority_guides.append(highest_priority_guide)

        del guides_ordered_name[priority_difference.index(max_difference)]
        del priority_difference[priority_difference.index(max_difference)]
        #print('Priority Difference: ', priority_difference)
        #print('Guide for', trip, role,': ', highest_priority_guide)
        #print('Calculated Priority: ', calculated_priority_guides)

    #print('Calculated Priority: ', calculated_priority_guides)
    return calculated_priority_guides


#get_ordered_priority_list(0,3)

################################################################################

def get_driver_priority_matrix():

    driver_dict = {}

    driver_object = session_guide.query(manage_staff.driver.driver)

    driver_list = [u.__dict__ for u in driver_object.all()]


    for num_drivers in range(len(driver_list)):

        if driver_list[num_drivers]['in_stream'] == 'true':

            driver_name = driver_list[num_drivers]['name']

            current_driver_priorities = []

            #x/y
            role_held_quotient = []

            #a/b
            trip_worked_quotient = []

            #sum(s(i)w(i))
            sum_weights = 0

            #s(i)
            s_of_i = []

            #d(i)
            d_of_i = []


            for x in range(len(create_schedule.schedule_dictionaries.trip_types)):

                #a
                times_trip_worked = []
                #b
                total_times_trip_worked = []

                for z in range(len(create_schedule.schedule_dictionaries.time_types)):

                    total_times_trip_worked.append(0)

                    times_trip_worked.append(0)

                    times_trip_worked[z] = driver_list[num_drivers]["driven_"
                                                +create_schedule.schedule_dictionaries.time_types[z]
                                                +create_schedule.schedule_dictionaries.trip_types[x]
                                            ]
                    print(driver_name, ' worked ', create_schedule.schedule_dictionaries.trip_types[x],' ', times_trip_worked[z], 'times')

                    for drivers in range(len(driver_list)):

                        total_times_trip_worked[z] += driver_list[drivers]["driven_"
                                                            +create_schedule.schedule_dictionaries.time_types[z]
                                                            +create_schedule.schedule_dictionaries.trip_types[x]]



                    print(' all guides worked ', create_schedule.schedule_dictionaries.trip_types[x],' ', total_times_trip_worked[z], 'times')

                    if total_times_trip_worked[z] != 0:

                        trip_worked_quotient.append(times_trip_worked[z]/total_times_trip_worked[z])

                    else:

                        trip_worked_quotient.append(0)


                    print('trip worked quotient for trip ', create_schedule.schedule_dictionaries.trip_types[x],
                          ' during ',create_schedule.schedule_dictionaries.time_types[z], ' is ', trip_worked_quotient[z])

                print(driver_list[num_drivers][create_schedule.schedule_dictionaries.trip_types[x]
                                            + "_seniority"])

                if driver_list[num_drivers][create_schedule.schedule_dictionaries.trip_types[x]
                                            + "_seniority"] == 1:

                    print("appended 1")
                    s_of_i.append(1)

                else:
                    print("appended 0")
                    s_of_i.append(0)

                if driver_list[num_drivers][create_schedule.schedule_dictionaries.trip_types[x]] == '1':

                    d_of_i.append(1)

                else:

                    d_of_i.append(0)

                print(driver_name, 'can ', d_of_i[x])

                print("s(i): ", s_of_i)
                print("trip_weight[x]: ",create_schedule.schedule_dictionaries.trip_weight[x])

                sum_weights += float(s_of_i[x])*create_schedule.schedule_dictionaries.trip_weight[x]


                print('sum_weights: ', sum_weights)
                print('trip_worked_quotient: ', trip_worked_quotient)
                print('d(i): ', d_of_i)



            for index in s_of_i:

                if s_of_i[index] == 0:

                    s_of_i[index] = 1

                else:

                    s_of_i[index] = 0

            x = 0

            for i in range(0,10,2):

                #print("#######################################################")
                #print("i: ", i)
                #print("trip_worked_quotient[i]*trip_worked_quotient[i+1]: ", (0.4)*(trip_worked_quotient[i]
        #        #    +trip_worked_quotient[i+1])**2)
        #        print("sum_weights: ", (0.2)*sum_weights)
        #        print("s_of_i[x]: ", (0.4)*s_of_i[x])
        #        print("d_of_i[x]: ", d_of_i[x])
        #        print("Final Priority: ", ((0.4)*(trip_worked_quotient[i]
        #            +trip_worked_quotient[i+1])**2
        #            +(0.4)*s_of_i[x]
        #        )*d_of_i[x])
        #        print("#######################################################")

                current_driver_priorities.append(
                                            (  (trip_worked_quotient[i]
                                                +trip_worked_quotient[i+1])**2
                                                +create_schedule.schedule_dictionaries.trip_weight[x]*s_of_i[x]
                                            )*d_of_i[x]
                                         )

                x+=1

                print('current driver priorities: ', i ,' ', current_driver_priorities)

            driver_dict[driver_name] = current_driver_priorities

    for driver in range(len(driver_list)):

        driver_name = driver_list[driver]['name']

        print(driver_name, ': ',driver_dict[driver_name][4])

    return driver_dict

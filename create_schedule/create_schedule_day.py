import create_schedule
from create_schedule import create_new_schedule
from create_schedule import schedule_util
from create_schedule import schedule_dictionaries
from create_schedule import create_schedule_role
from create_schedule import get_priority

import manage_staff
from manage_staff import staff_util
from manage_staff import guide
from manage_staff import driver

import popups
from popups import not_enough_guides_popup
from popups import not_enough_drivers_popup
from popups import overnight_popup

import os
import datetime
from PySide2 import QtCore, QtGui, QtWidgets
from shutil import copyfile

session_guide = guide.guide_session()
session_driver = driver.driver_session()
session_schedule = create_new_schedule.schedule_session()


def create_schedule_day(gui_window, scraper_object, current_date):
    """Create the schedule for all trips for the given day

    Parameters
    ----------
    gui_window : Ui_Form
        The Ui_Form object associated with the main gui
    scraper_object : scraper
        The scraper object used to extract data from the inputted excel file
    current_date : date
        A date object representing the date for which a schedule must be
        created

    Method Calls
    ------------
        -reset_this_period()
        -add_new_date()
        -calculate_previous_date()
        -get_total_guides()
        -get_total_drivers()
        -create_schedule_role()
        -copy_schedule_role()
    """

    #copyfile('trips.db', 'trips_backup.db')
    #copyfile('staff.db', 'staff_backup.db')

    #try:
    day_of_week = int(datetime.datetime.strptime(
            current_date, '%Y-%m-%d'
        ).strftime('%w')
      )

    print("DAY OF WEEK: ", day_of_week)

    if day_of_week == 0:
        print("MAKING SCHEDULE FOR MONDAY")
        manage_staff.staff_util.reset_this_period()

    current_date_object = create_new_schedule.add_new_date(current_date)
    temp_guide = 0
    print("\n")
    print("CREATING SHEDULE FOR ", current_date)
    trips = scraper_object.get_day(current_date)
    trip_role_assignment = {}
    class_IV_needed = {}
    num_clients = {}
    num_drivers = {}
    num_guides = {}
    num_class_IV_drivers = 0
    max_drivers = [0, 0, 0, 0,0,0,0,0]
    max_guides = [0, 0, 0, 0,0,0,0,0]
    num_safety = 0

    previous_date = schedule_util.calculate_previous_date(current_date)

    for trip_name in trips:
        num_clients[trip_name] = int(trips[trip_name])
        if trip_name == "Ticket to Ride - 09:30:00":

            if num_clients[trip_name] > 0:

                num_guides[trip_name] = int((num_clients[trip_name] // 10)
                                            + (num_clients[trip_name] % 10 > 0))

                num_drivers[trip_name] = int((num_clients[trip_name] // 20)
                                             + (num_clients[trip_name] % 20 > 0))

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

                if DialogBox.exec_():
                    trip_role_assignment = ui_guides.return_data()

            else:

                num_guides[trip_name] = 0
                num_drivers[trip_name] = 0

        else:

            num_guides[trip_name] = int((num_clients[trip_name] // 10)
                                        + (num_clients[trip_name] % 10 > 0))

            num_drivers[trip_name] = int((num_clients[trip_name] // 20)
                                         + (num_clients[trip_name] % 20 > 0))

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
            print("FOR: ", trip_name)
            print("NUMBER OF CLIENTS: ", num_clients[trip_name])
            print("NUMBER OF GUIDES NEEDED: ", num_guides[trip_name])
            print("NUMBER OF DRIVERS NEEDED: ", num_drivers[trip_name])
            print("\n")

    total_guides_needed = 0
    total_drivers_needed = 0

    for x in num_guides:
        total_guides_needed += num_guides[x]

    for x in num_drivers:
        total_drivers_needed += num_drivers[x]

    if total_guides_needed > len(manage_staff.staff_util.get_total_guides(session_guide)):
        DialogBox = QtWidgets.QDialog()
        ui_guides = popups.not_enough_guides_popup.Ui_not_enough_guides_popup()
        ui_guides.setupUi(DialogBox, DialogBox)
        DialogBox.show()

        if DialogBox.exec_():
            temp_guide = ui_guides.return_temp_guide()

            temp_guide_object = session_guide.query(manage_staff.guide.guide).filter(
                manage_staff.guide.guide.name.in_(
                    [temp_guide])).update(
                        {'in_stream': 'true'}, synchronize_session=False
            )

            session_guide.commit()

            print("\n")
            print("TEMP GUIDE INSTREAM SET TO TRUE: ", session_guide.query(
                manage_staff.guide.guide).filter(manage_staff.guide.guide.name.in_([temp_guide])))
            print("\n")

    if total_drivers_needed > len(manage_staff.staff_util.get_total_drivers(session_driver)):

        DialogBox = QtWidgets.QDialog()
        ui_drivers = popups.not_enough_drivers_popup.Ui_not_enough_drivers_popup()
        ui_drivers.setupUi(DialogBox, DialogBox)
        DialogBox.show()

        print("shown")

        if DialogBox.exec_():
            print("exec")
            temp_driver = ui_drivers.return_temp_driver()

            temp_driver_object = session_driver.query(manage_staff.driver.driver).filter(
                manage_staff.driver.driver.name.in_(
                    [temp_driver])).update(
                        {'in_stream':'true'},synchronize_session=False
                    )

            session_driver.commit()

            print("Set to true : ", session_driver.query(manage_staff.driver.driver).filter(manage_staff.driver.driver.name.in_([temp_driver])))

    for trip in create_schedule.schedule_dictionaries.trip_number_switch:

        if trip not in num_clients:

            num_clients[trip] = 0
            num_guides[trip] = 0
            num_drivers[trip] = 0

            print("\n")
            print("FOR: ", trip_name)
            print("NUMBER OF CLIENTS: ", num_clients)
            print("NUMBER OF GUIDES NEEDED: ", num_guides)
            print("NUMBER OF DRIVERS NEEDED: ", num_drivers)
            print("\n")

    num_class_IV_drivers = total_drivers_needed
    print("\n")
    print("NUM CLASS IV DRIVERS NEEDED: ", num_class_IV_drivers)

    total_drivers = manage_staff.staff_util.get_total_drivers(
        session_driver)
    drivers_with_class_IV = 0

    for index, value in enumerate(total_drivers):
        if total_drivers[index]['has_class_IV'] == '1':
            drivers_with_class_IV += 1

    print("DRIVERS WITH CLASS IV: ", drivers_with_class_IV)
    print("\n")

    trips_needing_class_IV_guide = 0
    if drivers_with_class_IV < num_class_IV_drivers:
        trips_needing_class_IV_guide = num_class_IV_drivers - drivers_with_class_IV

    for trip, value in enumerate(create_schedule.schedule_dictionaries.trip_types):
        if trip != 4:
            if (max_guides[trip] <= 4 and max_guides[trip] > 1):
                for role_needed in range(max_guides[trip]):
                    trips_needing_class_IV_guide = create_schedule_role.create_schedule_role(
                        role_needed, current_date, trip_role_assignment, trip, class_IV_needed, trips_needing_class_IV_guide)

            elif(max_guides[trip] == 1):

                trips_needing_class_IV_guide = create_schedule_role.create_schedule_role(
                    0, current_date, trip_role_assignment, trip, class_IV_needed, trips_needing_class_IV_guide)
                trips_needing_class_IV_guide = create_schedule_role.create_schedule_role(
                    4, current_date, trip_role_assignment, trip, class_IV_needed, trips_needing_class_IV_guide)

            for role_needed in range(max_drivers[trip]):
                trips_needing_class_IV_guide = create_schedule_role.create_schedule_role(
                    role_needed + 5, current_date, trip_role_assignment, trip, class_IV_needed, trips_needing_class_IV_guide)
    print("\n")
    print("CLASS IV NEEDED: ", class_IV_needed)
    print("\n")
    create_schedule.copy_schedule_role.copy_schedule_role(
        session_guide, session_driver, session_schedule,
        trips, trip_role_assignment, num_drivers, num_safety,
        num_clients, num_guides,
        max_guides, max_drivers, current_date_object, current_date)

    if temp_guide != 0:

        temp_guide_object = session_guide.query(manage_staff.guide.guide).filter(
            manage_staff.guide.guide.name.in_(
                [temp_guide])).update(
            {'in_stream': 'false'}, synchronize_session=False
        )

        session_guide.commit()
        print("\n")
        print("TEMP GUIDE INSTREAM RETURNED TO FALSE: ", session_guide.query(
            manage_staff.guide.guide).filter(manage_staff.guide.guide.name.in_([temp_guide])))
        print("\n")

        #   if temp_driver != 0:
        #
        #        temp_driver_object = session_driver.query(manage_staff.driver.driver).filter(
        #                                manage_staff.driver.driver.name.in_(
        #                                    [temp_driver])).update(
        #                                        {'in_stream':'false'},synchronize_session=False
        #                                    )
        #
        #        session_driver.commit()
        #
        #        print("TEMP DRIVER RETURNED TO FALSE: ", session_driver.query(manage_staff.driver.driver).filter(manage_staff.driver.driver.name.in_([temp_driver])))

        # os.remove('trips_backup.db')
        # os.remove('staff_backup.db')

    #except:

        #print("ERROR OCCURRED")

        #copyfile('trips_backup.db', 'trips.db')
        #copyfile('staff_backup.db', 'staff.db')
        # os.remove('trips_backup.db')
        # os.remove('staff_backup.db')

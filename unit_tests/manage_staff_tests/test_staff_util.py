import unittest
import os

import manage_staff
from manage_staff import guide

import create_schedule
from create_schedule import schedule_dictionaries

import sqlite3
import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import load_only

class TestStaffUtil(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        guide_test_engine = create_engine('sqlite:///staff_test.db', echo=False)
        guide_test_base = manage_staff.guide.guide_base
        guide_test_session = sessionmaker(bind=guide_test_engine)

        guide_test_base.metadata.create_all(guide_test_engine)
        cls.session_test_guide = guide_test_session()

        cls.test_guide = manage_staff.guide.guide(   name = "Test Guide", in_stream = 'true', has_class_IV = "1",
                                                tl_four_hour = "1", tl_c_wave = "1", tl_full_day = "1",
                                                tl_scenic_float = "1", tl_overnight = "1", guide_four_hour = "1", guide_c_wave = "1",
                                                guide_full_day = "1", guide_scenic_float = "1", guide_overnight = "1", safety_four_hour= "1",
                                                safety_c_wave = "1", safety_full_day= "1", safety_scenic_float = "1", safety_overnight = "1",
                                                tl_this_summer_four_hour = 1,
                                                tl_this_summer_c_wave = 1,
                                                tl_this_summer_full_day = 1,
                                                tl_this_summer_scenic_float = 1,
                                                tl_this_summer_overnight = 1,
                                                tl_this_period_four_hour = 1,
                                                tl_this_period_c_wave = 1,
                                                tl_this_period_full_day = 1,
                                                tl_this_period_scenic_float = 1,
                                                tl_this_period_overnight = 1,
                                                guided_this_summer_four_hour = 1, guided_this_summer_c_wave = 1,
                                                guided_this_summer_full_day = 1, guided_this_summer_scenic_float = 1,
                                                guided_this_summer_overnight = 1, guided_this_period_four_hour = 1,
                                                guided_this_period_c_wave = 1, guided_this_period_full_day = 1,
                                                guided_this_period_scenic_float = 1, guided_this_period_overnight = 1,
                                                safety_this_summer_four_hour = 1, safety_this_summer_c_wave = 1,
                                                safety_this_summer_full_day = 1, safety_this_summer_scenic_float=1,
                                                safety_this_summer_overnight = 1,
                                                safety_this_period_four_hour = 1, safety_this_period_c_wave = 1,
                                                safety_this_period_full_day = 1, safety_this_period_scenic_float = 1,
                                                safety_this_period_overnight = 1,
                                                days_since_last_day_off = 1
                                            )
        cls.session_test_guide.add(cls.test_guide)
        cls.session_test_guide.commit()

        driver_test_engine = create_engine('sqlite:///staff_test.db', echo=False)
        driver_test_base = manage_staff.driver.driver_base
        driver_test_session = sessionmaker(bind=driver_test_engine)

        driver_test_base.metadata.create_all(driver_test_engine)
        cls.session_test_driver = driver_test_session()

        cls.test_driver = manage_staff.driver.driver(    name = "Test Driver", in_stream = 'true',
                                                    has_class_IV = "1", four_hour = "1",
                                                    c_wave = "1", full_day = "1",
                                                    scenic_float = "1", overnight = "1",
                                                    four_hour_seniority = "1",
                                                    c_wave_seniority = "1", full_day_seniority = "1",
                                                    scenic_float_seniority = "1", overnight_seniority = "1",
                                                    driven_this_summer_four_hour = 1,
                                                    driven_this_summer_c_wave = 1,
                                                    driven_this_summer_full_day = 1,
                                                    driven_this_summer_scenic_float = 1,
                                                    driven_this_summer_overnight = 1,
                                                    driven_this_period_four_hour = 1,
                                                    driven_this_period_c_wave = 1,
                                                    driven_this_period_full_day = 1,
                                                    driven_this_period_scenic_float = 1,
                                                    driven_this_period_overnight = 1,
                                                    days_since_last_day_off = 1,
                                            )

        cls.session_test_driver.add(cls.test_driver)
        cls.session_test_driver.commit()

        schedule_test_engine = create_engine('sqlite:///schedule_test.db', echo=False)
        schedule_test_base = create_schedule.create_new_schedule.schedule_base
        schedule_test_session = sessionmaker(bind=schedule_test_engine)

        schedule_test_base.metadata.create_all(schedule_test_engine)
        cls.session_test_schedule = schedule_test_session()

        cls.test_schedule = create_schedule.create_new_schedule.schedule( date = "2019-07-22",
                                            period = 9,
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

        cls.session_test_schedule.add(cls.test_schedule)
        cls.session_test_schedule.commit()



    def test_update_num_trips_guide(self):
        print("GUIDE #################################################################")
        manage_staff.staff_util.update_num_trips_guide(self.session_test_guide, self.session_test_schedule, "Test Guide", 0, 1, 0, "2019-05-22")

        for time_types in range(0,2):
            trip_count_object = self.session_test_guide.query(manage_staff.guide.guide).filter(
                                manage_staff.guide.guide.name == "Test Guide").options(load_only(
                                    create_schedule.schedule_dictionaries.guide_roles[0]
                                    +create_schedule.schedule_dictionaries.time_types[time_types]
                                    +create_schedule.schedule_dictionaries.trip_types[0]
                                ))
            trip_count_list = [u.__dict__ for u in trip_count_object.all()]
            trip_count = trip_count_list[0][create_schedule.schedule_dictionaries.guide_roles[0]
                                          +create_schedule.schedule_dictionaries.time_types[time_types]
                                          +create_schedule.schedule_dictionaries.trip_types[0]]

            if time_types == 0:
                print(trip_count, "== ", 2,"??")
                self.assertEqual(trip_count, 2)
            elif time_types == 1:
                print(trip_count, "== ", 0,"??")
                self.assertEqual(trip_count, 0)

    def test_update_num_trips_guide_same_period(self):
        print("GUIDE SAME PERIOD######################################################")
        manage_staff.staff_util.update_num_trips_guide(self.session_test_guide, self.session_test_schedule, "Test Guide", 0, 1, 0, "2019-07-22")

        for time_types in range(0,2):
            trip_count_object = self.session_test_guide.query(manage_staff.guide.guide).filter(
                                manage_staff.guide.guide.name == "Test Guide").options(load_only(
                                    create_schedule.schedule_dictionaries.guide_roles[0]
                                    +create_schedule.schedule_dictionaries.time_types[time_types]
                                    +create_schedule.schedule_dictionaries.trip_types[0]
                                ))
            trip_count_list = [u.__dict__ for u in trip_count_object.all()]
            trip_count = trip_count_list[0][create_schedule.schedule_dictionaries.guide_roles[0]
                                          +create_schedule.schedule_dictionaries.time_types[time_types]
                                          +create_schedule.schedule_dictionaries.trip_types[0]]

            if time_types == 0:
                print(trip_count, "== ", 3,"??")
                self.assertEqual(trip_count, 3)
            elif time_types == 1:
                print(trip_count, "== ", 1,"??")
                self.assertEqual(trip_count, 1)


    def test_update_num_trips_driver(self):
        print("DRIVER################################################################")
        manage_staff.staff_util.update_num_trips_driver(self.session_test_driver, self.session_test_schedule, "Test Driver", 0, 1, "2019-05-22")

        for time_types in range(0,2):
            trip_count_object = self.session_test_driver.query(manage_staff.driver.driver).filter(
                                    manage_staff.driver.driver.name == "Test Driver").options(
                                        load_only(
                                            "driven_"
                                            +create_schedule.schedule_dictionaries.time_types[time_types]
                                            +create_schedule.schedule_dictionaries.trip_types[0]
                                        )
                                    )

            trip_count_list = [u.__dict__ for u in trip_count_object.all()]

            trip_count = trip_count_list[0]["driven_"
                                          +create_schedule.schedule_dictionaries.time_types[time_types]
                                          +create_schedule.schedule_dictionaries.trip_types[0]]

            if time_types == 0:
                print(trip_count, "== ", 2,"??")
                self.assertEqual(trip_count, 2)
            elif time_types == 1:
                print(trip_count, "== ", 0,"??")
                self.assertEqual(trip_count, 0)


    def test_update_num_trips_driver_same_period(self):
        print("DRIVER SAME PERIOD####################################################")
        manage_staff.staff_util.update_num_trips_driver(self.session_test_driver, self.session_test_schedule, "Test Driver", 0, 1, "2019-07-22")

        for time_types in range(0,2):
            trip_count_object = self.session_test_driver.query(manage_staff.driver.driver).filter(
                                    manage_staff.driver.driver.name == "Test Driver").options(
                                        load_only(
                                            "driven_"
                                            +create_schedule.schedule_dictionaries.time_types[time_types]
                                            +create_schedule.schedule_dictionaries.trip_types[0]
                                        )
                                    )

            trip_count_list = [u.__dict__ for u in trip_count_object.all()]

            trip_count = trip_count_list[0]["driven_"
                                          +create_schedule.schedule_dictionaries.time_types[time_types]
                                          +create_schedule.schedule_dictionaries.trip_types[0]]

            if time_types == 0:
                print(trip_count, "== ", 3,"??")
                self.assertEqual(trip_count, 3)
            elif time_types == 1:
                print(trip_count, "== ", 1,"??")
                self.assertEqual(trip_count, 1)

    def test_reset_period(self):
        print("RESET#################################################################")
        manage_staff.staff_util.reset_this_period(self.session_test_guide, self.session_test_driver)

        for trip in create_schedule.schedule_dictionaries.trip_types:

            period_count_object = self.session_test_driver.query(manage_staff.driver.driver).filter(
                                    manage_staff.driver.driver.name == "Test Driver").options(
                                        load_only(
                                            "driven_"
                                            +create_schedule.schedule_dictionaries.time_types[1]
                                            +create_schedule.schedule_dictionaries.trip_types[trip]
                                        )
                                    )
            period_count_list = [u.__dict__ for u in period_count_object.all()]
            period_count = period_count_list[0]["driven_"
                                          +create_schedule.schedule_dictionaries.time_types[1]
                                          +create_schedule.schedule_dictionaries.trip_types[trip]]

            self.assertEqual(period_count, 0)

            period_count_object = self.session_test_guide.query(manage_staff.guide.guide).filter(
                                manage_staff.guide.guide.name == "Test Guide").options(load_only(
                                    create_schedule.schedule_dictionaries.guide_roles[0]
                                    +create_schedule.schedule_dictionaries.time_types[1]
                                    +create_schedule.schedule_dictionaries.trip_types[0]
                                ))
            period_count_list = [u.__dict__ for u in period_count_object.all()]
            period_count = period_count_list[0][create_schedule.schedule_dictionaries.guide_roles[0]
                                          +create_schedule.schedule_dictionaries.time_types[1]
                                          +create_schedule.schedule_dictionaries.trip_types[0]]

            self.assertEqual(period_count, 0)

    @classmethod
    def tearDownClass(cls):
        print("tear")
        cls.session_test_guide.close()
        cls.session_test_driver.close()
        cls.session_test_schedule.close()
        os.remove("staff_test.db")
        os.remove("schedule_test.db")

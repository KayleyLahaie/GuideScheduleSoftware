import unittest
import create_schedule.schedule_util


class TestScheduleUtil(unittest.TestCase):

    # test if the calculate_previous_date() method returns accurate results
    def test_previous_date(self):
        self.assertEqual(create_schedule.schedule_util.calculate_previous_date("2019-04-12"), "2019-04-11")
        self.assertEqual(create_schedule.schedule_util.calculate_previous_date("2019-05-01"), "2019-04-30")

    # tes if the calculate_next_date() method returns accurate results
    def test_next_date(self):
        self.assertEqual(create_schedule.schedule_util.calculate_next_date("2019-07-30"), "2019-07-31")
        self.assertEqual(create_schedule.schedule_util.calculate_next_date("2019-04-30"), "2019-05-01")
        self.assertEqual(create_schedule.schedule_util.calculate_next_date("2019-02-28"), "2019-03-01")

    # test if the get_current_period() method returns accurate results
    def test_current_period(self):
        self.assertEqual(create_schedule.schedule_util.get_current_period("2019-05-15"), 0)
        self.assertEqual(create_schedule.schedule_util.get_current_period("2019-05-21"), 0)
        self.assertEqual(create_schedule.schedule_util.get_current_period("2019-07-22"), 9)
        self.assertEqual(create_schedule.schedule_util.get_current_period("2019-08-22"), 14)

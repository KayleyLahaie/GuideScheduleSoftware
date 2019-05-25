import datetime
import create_schedule


column_label = []
schedule_list = []

def load_schedule_data(session_schedule, start_date, end_date):
    """Queries the schedule table in trips.db for rows that fall in between the
    start and end dates and loads the gathered data into a table in the
    View Staff widget

    Parameters
    ----------
        start_date: str
            A string representation of the first date to be queried,
            formatted as YYYY-MM-DD
        end_date: str
            A string representation of the last date to be queried,
            formatted as YYYY-MM-DD
    """

    global column_label
    column_label = [0, 0, 0, 0, 0, 0, 0]
    global schedule_list
    schedule_list = []
    day_of_week = int(datetime.datetime.strptime(
        start_date, '%Y-%m-%d').strftime('%w'))

    column_number = day_of_week

    column_label.insert(column_number, start_date)
    del column_label[day_of_week+1]

    current_date = start_date
    for day in range(day_of_week + 1, 7):
        column_label.insert(
            day, create_schedule.schedule_util.calculate_next_date(current_date))
        del column_label[day + 1]
        current_date = create_schedule.schedule_util.calculate_next_date(
            current_date)

    current_date = start_date
    for day in range(0, day_of_week):
        column_label.insert(
            day_of_week-day-1, create_schedule.schedule_util.calculate_previous_date(current_date))
        del column_label[day_of_week-day]
        current_date = create_schedule.schedule_util.calculate_previous_date(current_date)

    start_date = column_label[0]
    if end_date > column_label[6]:
        end_date = column_label[6]
    else:
        end_date = create_schedule.schedule_util.calculate_next_date(end_date)

    while start_date != end_date:

        print(start_date)

        schedule_object = session_schedule.query(create_schedule.create_new_schedule.schedule).filter(create_schedule.create_new_schedule.schedule.date==start_date)
        schedule_list_item = [u.__dict__ for u in schedule_object.all()]

        if len(schedule_list_item) != 0:
            schedule_list.append(schedule_list_item[0])
            print(schedule_list_item)
        else:
            blank_object = create_schedule.create_new_schedule.schedule( date = start_date,
                                                period = 0,
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
                                                second_driver_scenic_float_09 = '',
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
            session_schedule.add(blank_object)
            session_schedule.commit()
            blank_object = session_schedule.query(create_schedule.create_new_schedule.schedule).filter(create_schedule.create_new_schedule.schedule.date==start_date)
            schedule_list_item_blank = [u.__dict__ for u in blank_object.all()]
            print(schedule_list_item_blank)
            schedule_list.append(schedule_list_item_blank[0])
            session_schedule.query(create_schedule.create_new_schedule.schedule).filter(
                        create_schedule.create_new_schedule.schedule.date==start_date
                    ).delete(synchronize_session=False)
        start_date = create_schedule.schedule_util.calculate_next_date(start_date)

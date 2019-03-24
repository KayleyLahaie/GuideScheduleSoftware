trip_weight = {
    0: 0.25,
    1: 0.15,
    2: 0.45,
    3: 0.10,
    4: 0.05,
}

guide_roles = {
    0: 'tl_',
    1: 'guided_',
    2: 'safety_',
}

driver_roles = {
    0: 'first_',
    1: 'second_',
}


guide_roles_converter = {
    0: 0,
    1: 1,
    2: 1,
    3: 1,
    4: 2,
    }

guide_roles_2 = {
    0: 'tl_',
    1: 'guide_',
    2: 'safety_',
}

time_types = {
    0: 'this_summer_',
    1: 'this_period_',
}

trip_types = {
    0: 'four_hour',
    1: 'c_wave',
    2: 'full_day',
    3: 'scenic_float',
    4: 'overnight',
}

role_update_switch = {
    0: 0,
    1: 1,
    2: 1,
    3: 1,
    4: 2,
    5: 0,
    6: 0,

}

max_guides_trip_swictch = {
        'Ready Set Go - 4 Hour - 10:00:00': 0,
        'Ready Set Go - 4 Hour - 14:00:00': 0,
        'Catch A Wave - 10:00:00': 1,
        'Catch A Wave - 14:00:00': 1,
        'Guaranteed Addiction - 09:30:00': 2,
        'Take it Easy - Scenic Float - 09:00:00': 3,
        'Take it Easy - Scenic Float - 13:00:00': 3,
        'Ticket to Ride - 09:30:00': 4,
}

trip_name_switch = {
    0: 'Ready Set Go - 4 Hour - 10:00:00',
    1: 'Ready Set Go - 4 Hour - 14:00:00',
    2: 'Catch A Wave - 10:00:00',
    3: 'Catch A Wave - 14:00:00',
    4: 'Guaranteed Addiction - 09:30:00',
    5: 'Take it Easy - Scenic Float - 09:00:00',
    6: 'Take it Easy - Scenic Float - 13:00:00',
    7: 'Ticket to Ride - 09:30:00',
    }

trip_number_switch = {
        'Ready Set Go - 4 Hour - 10:00:00': 0,
        'Ready Set Go - 4 Hour - 14:00:00': 1,
        'Catch A Wave - 10:00:00': 2,
        'Catch A Wave - 14:00:00': 3,
        'Guaranteed Addiction - 09:30:00': 4,
        'Take it Easy - Scenic Float - 09:00:00': 5,
        'Take it Easy - Scenic Float - 13:00:00': 6,
        'Ticket to Ride - 09:30:00': 7,
}

num_trips_guided_switch_excel_summer = {
    'Ready Set Go - 4 Hour - 10:00:00': 'guided_this_summer_four_hour',
    'Ready Set Go - 4 Hour - 14:00:00': 'guided_this_summer_four_hour',
    'Catch A Wave - 10:00:00': 'guided_this_summer_c_wave',
    'Catch A Wave - 14:00:00': 'guided_this_summer_c_wave',
    'Guaranteed Addiction - 09:30:00': 'guided_this_summer_full_day',
    'Take it Easy - Scenic Float - 09:00:00': 'guided_this_summer_scenic_float',
    'Take it Easy - Scenic Float - 13:00:00': 'guided_this_summer_scenic_float',
    'Ticket to Ride - 09:30:00': 'guided_this_summer_overnight',
}

num_trips_guided_switch_excel_period = {
    'Ready Set Go - 4 Hour - 10:00:00': 'guided_this_period_four_hour',
    'Ready Set Go - 4 Hour - 14:00:00': 'guided_this_period_four_hour',
    'Catch A Wave - 10:00:00': 'guided_this_period_c_wave',
    'Catch A Wave - 14:00:00': 'guided_this_period_c_wave',
    'Guaranteed Addiction - 09:30:00': 'guided_this_period_full_day',
    'Take it Easy - Scenic Float - 09:00:00': 'guided_this_period_scenic_float',
    'Take it Easy - Scenic Float - 13:00:00': 'guided_this_period_scenic_float',
    'Ticket to Ride - 09:30:00': 'guided_this_period_overnight',
}

num_trips_safety_switch_excel_summer = {
    'Ready Set Go - 4 Hour - 10:00:00': 'safety_this_summer_four_hour',
    'Ready Set Go - 4 Hour - 14:00:00': 'safety_this_summer_four_hour',
    'Catch A Wave - 10:00:00': 'safety_this_summer_c_wave',
    'Catch A Wave - 14:00:00': 'safety_this_summer_c_wave',
    'Guaranteed Addiction - 09:30:00': 'safety_this_summer_full_day',
    'Take it Easy - Scenic Float - 09:00:00': 'safety_this_summer_scenic_float',
    'Take it Easy - Scenic Float - 13:00:00': 'safety_this_summer_scenic_float',
    'Ticket to Ride - 09:30:00': 'safety_this_summer_overnight',
}

num_trips_safety_switch_excel_period = {
    'Ready Set Go - 4 Hour - 10:00:00': 'safety_this_period_four_hour',
    'Ready Set Go - 4 Hour - 14:00:00': 'safety_this_period_four_hour',
    'Catch A Wave - 10:00:00': 'safety_this_period_c_wave',
    'Catch A Wave - 14:00:00': 'safety_this_period_c_wave',
    'Guaranteed Addiction - 09:30:00': 'safety_this_period_full_day',
    'Take it Easy - Scenic Float - 09:00:00': 'safety_this_period_scenic_float',
    'Take it Easy - Scenic Float - 13:00:00': 'safety_this_period_scenic_float',
    'Ticket to Ride - 09:30:00': 'safety_this_period_overnight',
}

num_trips_driven_switch_excel_summer = {
    'Ready Set Go - 4 Hour - 10:00:00': 'driven_this_summer_four_hour',
    'Ready Set Go - 4 Hour - 14:00:00': 'driven_this_summer_four_hour',
    'Catch A Wave - 10:00:00': 'driven_this_summer_c_wave',
    'Catch A Wave - 14:00:00': 'driven_this_summer_c_wave',
    'Guaranteed Addiction - 09:30:00': 'driven_this_summer_full_day',
    'Take it Easy - Scenic Float - 09:00:00': 'driven_this_summer_scenic_float',
    'Take it Easy - Scenic Float - 13:00:00': 'driven_this_summer_scenic_float',
    'Ticket to Ride - 09:30:00': 'driven_this_summer_overnight',
}

num_trips_driven_switch_excel_period = {
    'Ready Set Go - 4 Hour - 10:00:00': 'driven_this_period_four_hour',
    'Ready Set Go - 4 Hour - 14:00:00': 'driven_this_period_four_hour',
    'Catch A Wave - 10:00:00': 'driven_this_period_c_wave',
    'Catch A Wave - 14:00:00': 'driven_this_period_c_wave',
    'Guaranteed Addiction - 09:30:00': 'driven_this_period_full_day',
    'Take it Easy - Scenic Float - 09:00:00': 'driven_this_period_scenic_float',
    'Take it Easy - Scenic Float - 13:00:00': 'driven_this_period_scenic_float',
    'Ticket to Ride - 09:30:00': 'driven_this_period_overnight',
}

role_switch = {
    0: 'trip_leader',
    1: 'second_guide',
    2: 'third_guide',
    3: 'fourth_guide',
    4: 'safety',
    5: 'first_driver',
    6: 'second_driver',
}

role_switch_header = {
    0: 'trip leader',
    1: 'second guide',
    2: 'third guide',
    3: 'fourth guide',
    4: 'safety',
    5: 'first driver',
    6: 'second driver',
}

trip_switch_numerical = {
    0: '_ready_set_go_10',
    1: '_ready_set_go_14',
    2: '_c_wave_10',
    3: '_c_wave_14',
    4: '_guaranteed_addiction_930',
    5: '_scenic_float_09',
    6: '_scenic_float_13',
    7: '_overnight_930',
}

trip_switch_numerical_header = {
    0: ' - RSG (10)',
    1: ' - RSG (14)',
    2: ' - CWave (10)',
    3: ' - CWave (14)',
    4: ' - FD (9:30)',
    5: ' - Float (9)',
    6: ' - Float (13)',
    7: ' - Overnight (9:30)',
}

trip_switch_excel = {
    'Ready Set Go - 4 Hour - 10:00:00': '_ready_set_go_10',
    'Ready Set Go - 4 Hour - 14:00:00': '_ready_set_go_14',
    'Catch A Wave - 10:00:00': '_c_wave_10',
    'Catch A Wave - 14:00:00': '_c_wave_14',
    'Guaranteed Addiction - 09:30:00': '_guaranteed_addiction_930',
    'Take it Easy - Scenic Float - 09:00:00': '_scenic_float_09',
    'Take it Easy - Scenic Float - 13:00:00': '_scenic_float_13',
    'Ticket to Ride - 09:30:00': '_overnight_930',
}

overnight_dialog_guide_labels = {
    0: 'trip leader',
    1: 'second guide',
    2: 'third guide',
    3: 'fourth guide',
}

overnight_dialog_guide_text_name = {
    0: 'trip_leader_name',
    1: 'second_guide_name',
    2: 'third_guide_name',
    3: 'fourth_guide_name',
}

overnight_dialog_guide_label_name = {
    0: 'trip_leader_label',
    1: 'second_guide_label',
    2: 'third_guide_label',
    3: 'fourth_guide_label',
}

view_staff_headers = {
    0:"Ready Set Go - 10am",
    1:"Ready Set Go - 2pm",
    2:"Catch a Wave - 10am",
    3:"Catch a Wave - 2pm",
    4:"Guaranteed Addiction",
    5:"Take it Easy - 9am",
    6:"Take it Easy - 1pm",
    7:"Ticket to Ride",
}

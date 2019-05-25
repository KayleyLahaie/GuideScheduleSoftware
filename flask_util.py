from flask import Flask
from flask import request
from flask import render_template

import load_schedule_data

import create_schedule
from create_schedule import schedule_dictionaries

app = Flask(__name__)

@app.route('/schedule.html')
def my_form():
    column_label = load_schedule_data.column_label
    schedule_list = load_schedule_data.schedule_list

    row_label = [
                'trip_leader_ready_set_go_10' ,
                'second_guide_ready_set_go_10' ,
                'third_guide_ready_set_go_10' ,
                'fourth_guide_ready_set_go_10' ,
                'safety_ready_set_go_10' ,
                'first_driver_ready_set_go_10' ,
                'second_driver_ready_set_go_10' ,
                'trip_leader_ready_set_go_14' ,
                'second_guide_ready_set_go_14' ,
                'third_guide_ready_set_go_14' ,
                'fourth_guide_ready_set_go_14' ,
                'safety_ready_set_go_14',
                'first_driver_ready_set_go_14',
                'second_driver_ready_set_go_14',
                'trip_leader_c_wave_10',
                'second_guide_c_wave_10',
                'third_guide_c_wave_10',
                'fourth_guide_c_wave_10',
                'safety_c_wave_10',
                'first_driver_c_wave_10',
                'second_driver_c_wave_10',
                'trip_leader_c_wave_14',
                'second_guide_c_wave_14',
                'third_guide_c_wave_14',
                'fourth_guide_c_wave_14',
                'safety_c_wave_14',
                'first_driver_c_wave_14',
                'second_driver_c_wave_14',
                'trip_leader_guaranteed_addiction_930',
                'second_guide_guaranteed_addiction_930',
                'third_guide_guaranteed_addiction_930',
                'fourth_guide_guaranteed_addiction_930',
                'safety_guaranteed_addiction_930',
                'first_driver_guaranteed_addiction_930',
                'second_driver_guaranteed_addiction_930',
                'trip_leader_scenic_float_09',
                'second_guide_scenic_float_09',
                'third_guide_scenic_float_09',
                'fourth_guide_scenic_float_09',
                'safety_scenic_float_09',
                'first_driver_scenic_float_09',
                'second_driver_scenic_float_09',
                'trip_leader_scenic_float_13',
                'second_guide_scenic_float_13',
                'third_guide_scenic_float_13',
                'fourth_guide_scenic_float_13',
                'safety_scenic_float_13',
                'first_driver_scenic_float_13',
                'second_driver_scenic_float_13',
                'trip_leader_overnight_930',
                'second_guide_overnight_930',
                'third_guide_overnight_930',
                'fourth_guide_overnight_930',
                'safety_overnight_930',
                'first_driver_overnight_930',
                'second_driver_overnight_930',
            ]

    return render_template("schedule.html", column_label = column_label,
                            view_staff_headers = create_schedule.schedule_dictionaries.view_staff_headers,
                            role_switch_header = create_schedule.schedule_dictionaries.role_switch_header,
                            schedule_list = schedule_list,
                            row_label = row_label)

@app.route('/schedule.html', methods=['POST'])
def my_form_post():
    name = request.form['name']
    role = request.form['role']
    current_date = request.form['current_date']
    print("POST recieved - Role, Current Date: ", role, current_date)



    #freezer.freeze()

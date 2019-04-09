import datetime

################################################################################

def calculate_previous_date(current_date):

    last_digit = current_date[-1]

    if(last_digit == '0'):
        second_last_digit = int(current_date[-2]) - 1
        last_digit = '9'
        new_date = current_date[:8] +str(second_last_digit)+ str(last_digit)
    else:
        last_digit = int(last_digit) - 1
        new_date = current_date[:9] + str(last_digit)

    return new_date


################################################################################

def calculate_next_date(previous_date):

    last_digit = previous_date[-1]

    if(last_digit == '9'):
        second_last_digit = int(previous_date[-2]) + 1
        last_digit = '0'
        new_date = previous_date[:8] +str(second_last_digit)+ str(last_digit)
    else:
        last_digit = int(last_digit) + 1
        new_date = previous_date[:9] + str(last_digit)

    return new_date


################################################################################
def get_current_period(current_date):

    print("CURRENT DATE - GET CURRENT PERIOD: ", current_date)
    season_start_date_object =  datetime.date(datetime.datetime.now().year, 5, 15)
    current_date_object = datetime.date(int(current_date[0:3]), int(current_date[5:6]), int(current_date[8:9]))
    difference = current_date_object - season_start_date_object

    current_period = ceil(difference.days/7)
    print("CURRENT PERIOT - GET CURRENT PERIOD: ", current_period)
    return current_period

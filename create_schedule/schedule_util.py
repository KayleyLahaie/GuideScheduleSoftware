import datetime
import math
from datetime import timedelta


################################################################################

def calculate_previous_date(current_date):

    year = int(current_date[0:4])
    month = int(current_date[5:7])
    day = int(current_date[8:10])
    current_date_object = datetime.date(year, month, day)

    return datetime.datetime.strftime(current_date_object - timedelta(1), '%Y-%m-%d')



################################################################################

def calculate_next_date(previous_date):

    year = int(previous_date[0:4])
    month = int(previous_date[5:7])
    day = int(previous_date[8:10])
    previous_date_object = datetime.date(year, month, day)

    return datetime.datetime.strftime(previous_date_object + timedelta(1), '%Y-%m-%d')


################################################################################
def get_current_period(current_date):

    print("\n#########################################################")
    print("GETTING THE CURRENT PERIOD")
    print("CURRENT DATE: ", current_date)
    season_start_date_object =  datetime.date(datetime.datetime.now().year, 5, 15)
    year = int(current_date[0:4])
    month = int(current_date[5:7])
    day = int(current_date[8:10])
    current_date_object = datetime.date(year, month, day)
    difference =  season_start_date_object - current_date_object
    current_period = math.floor((-difference.days)/7)
    print("CURRENT PERIOD: ", current_period)
    print("#########################################################\n")
    return current_period

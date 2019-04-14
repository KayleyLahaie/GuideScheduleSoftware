import datetime
import math
from datetime import timedelta

def calculate_previous_date(current_date):
    """Determine the date previous to the inputted date

    Parameters
    ----------
    current_date: str
        A string representing a date formatted as YYYY-MM-DD

    Returns
    ------
    str
        A string representing the date previous to the inputted date in the
        format YYYY-MM-DD
    """
    
    year = int(current_date[0:4])
    month = int(current_date[5:7])
    day = int(current_date[8:10])
    current_date_object = datetime.date(year, month, day)

    return datetime.datetime.strftime(current_date_object - timedelta(1), '%Y-%m-%d')

def calculate_next_date(previous_date):
    """Determine the next date after the inputted date

    Parameters
    ----------
    current_date: str
        A string representing a date formatted as YYYY-MM-DD

    Returns
    ------
    str
        A string representing the next date after the inputted date in the
        format YYYY-MM-DD
    """

    year = int(previous_date[0:4])
    month = int(previous_date[5:7])
    day = int(previous_date[8:10])
    previous_date_object = datetime.date(year, month, day)

    return datetime.datetime.strftime(previous_date_object + timedelta(1), '%Y-%m-%d')

def get_current_period(current_date):
    """Calculate the period number in which the inpuuted date falls

    Parameters
    ----------
    current_date: str
        A string representing a date formatted as YYYY-MM-DD

    Returns
    ------
    int
        An integer values representing the number of weeks since the start of the season
    """

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

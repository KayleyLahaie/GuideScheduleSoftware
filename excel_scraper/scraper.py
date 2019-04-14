import xlrd
from datetime import time
import datetime

class excel_scraper:
    """
    Produces a scraper object that can extract necessary data from excel sheet

    Attributes
    ----------
    file_path : str
        A string representing the path to the input file
    workbook : workbook
        A workbook object allowing access to the input file
    sheet : sheet
        A sheet object allowing access to the first sheet in workbook
    num_rows : int
        The number of rows in the sheet

    Methods
    -------
    get_first_date(self)
        Extracts the first date listed in the excel file

    get_num_days(self)
        Determines the number of days represented in the excel sheet

    get_day(self, current_date)
        Determines which trips are booked for the current date

    get_new_offset(self, current_date)
        Determines the cell index where the data for the current date begins

    get_trip(self, offset)
        Extracts the name and time of the trip starting at the offset and
        determines at which index the trip ends

    get_num_clients(self, trip_start, trip_offset)
        Sums the number of clients booked in each group for the total number
        of clients
    """

    def __init__(self, new_file_path):
        """
        Parameters
        ----------
        new_file_path: str
            The string representing the path to the input file, provided by The
            user
        """

        self.file_path = new_file_path
        self.workbook = xlrd.open_workbook(self.file_path)
        self.sheet = self.workbook.sheet_by_index(0)
        self.num_rows = self.sheet.nrows

    def get_first_date(self):
        """Extracts the first date listed in the excel file

        Retrieves the first date by extracting an xldate tuple from cell (2, 5)
        as a datetime object, then converting it into an isoformatted date
        object

        Returns
        ------
        date
           a date object created from the datetime object extracted from the
           excel sheet
        """

        date = datetime.datetime(
                    *xlrd.xldate_as_tuple(
                        self.sheet.cell_value(2, 5),
                        self.workbook.datemode
                    )
                )
        first_date = date.date().isoformat()

        return first_date


    def get_num_days(self):
        """Determines the number of days represented in the excel sheet

        Starts by creating date objects representing the last and first datse
        in the file and subtracts the first from the last to determine the
        total number of days

        Method Calls
        ------------
            -get_first_date()

        Returns
        ------
        int
            an integer count of the number of days represented in the file
        """

        last_row = int(self.sheet.nrows)
        last_row-=2

        date = datetime.datetime(
                    *xlrd.xldate_as_tuple(
                        self.sheet.cell_value(last_row, 5),
                        (self.workbook.datemode)
                    )
                )

        last_date = date.date().isoformat()
        last_date_digits = int(last_date[-2:])
        first_date = self.get_first_date()
        first_date_digits = int(first_date[-2:])

        if(last_date_digits >= first_date_digits):
            num_days = last_date_digits - first_date_digits + 1

        return num_days



    def get_day(self, current_date):
        """Determines which trips are booked for the current date

        Creates a dictionary containing trip names and the number of clients
        booked using the get_trips() method

        Parameters
        ----------
        current_date : date
            A date object representing the date currently being scheduled

        Method Calls
        ------------
            -get_trip()

        Returns
        ------
        dict
            an dictionary containing trip names and number of clients
        """

        trips = {'Ready Set Go - 4 Hour - 10:00:00': 0,
                'Ready Set Go - 4 Hour - 14:00:00': 0,
                'Catch A Wave - 10:00:00': 0,
                'Catch A Wave - 14:00:00': 0,
                'Guaranteed Addiction - 09:30:00': 0,
                'Take it Easy - Scenic Float - 09:00:00': 0,
                'Take it Easy - Scenic Float - 13:00:00': 0,
                'Ticket to Ride - 09:30:00': 0,
                }

        offset = self.get_new_offset(current_date)

        temp_tuple = self.get_trip(offset)
        trips[temp_tuple[0]] = temp_tuple[1]

        current_date = self.sheet.cell_value(offset, 5)
        desired_date = self.sheet.cell_value(offset, 5)

        while current_date == desired_date:
            current_date = self.sheet.cell_value(temp_tuple[2]+1, 5)
            if(current_date == desired_date):
                temp_tuple = self.get_trip(temp_tuple[2])
                trips[temp_tuple[0]] = temp_tuple[1]

        print("###################################################################")
        for x in trips:
            print (x, trips[x])
        print("###################################################################")

        return trips


    def get_new_offset(self, current_date):
        """Determines the cell index where the data for the current date begins

        Parameters
        ----------
        current_date : date
            A date object representing the date currently being scheduled

        Returns
        ------
        int
            an integer value representing the row number where the data for the
            date being scheduled starts
        """

        default_offset = 2;
        new_date = datetime.datetime(
                        *xlrd.xldate_as_tuple(
                            self.sheet.cell_value(default_offset, 5),
                            self.workbook.datemode
                        )
                    )
        date = new_date.date().isoformat()

        while date != current_date:
            default_offset+=1
            new_date = datetime.datetime(
                            *xlrd.xldate_as_tuple(
                                self.sheet.cell_value(default_offset, 5),
                                self.workbook.datemode
                            )
                        )
            date = new_date.date().isoformat()

        return default_offset


    def get_trip(self, offset):
        """Creates a tuple containing the name and time of the trip that starts
        at the offset, the number of clients on the trip, at the row number
        where the next trip ???starts???

        Parameters
        ----------
        offset : int
            An integer representing the row number where the data for the
            current trip starts

        Method Calls
        ------------
            -get_num_clients()

        Returns
        ------
        tuple
            A tuple containing a string representation of the trip name, the
            number of clients and the offset
        """

        trip_start = offset
        trip_offset = offset

        trip_time = xlrd.xldate_as_tuple(
                        self.sheet.cell_value(trip_offset, 7),
                        self.workbook.datemode
                    )
        trip_time_date = datetime.datetime(
                            *xlrd.xldate_as_tuple(
                                self.sheet.cell_value(trip_offset, 5),
                                self.workbook.datemode
                            )
                        )
        date = trip_time_date.date().isoformat()

        trip_time = time(*trip_time[3:])
        current_trip_time = trip_time

        current_trip = self.sheet.cell_value(trip_start, 4)
        desired_trip = self.sheet.cell_value(trip_start, 4)

        while current_trip == desired_trip:
            if(current_trip_time != trip_time):
                break

            else:
                rows = self.sheet.nrows

                if trip_offset < rows-2:
                    trip_offset+= 1

                    if self.sheet.cell_type(trip_offset, 7) != 0:
                        temp_trip_time = xlrd.xldate_as_tuple(
                                            self.sheet.cell_value(trip_offset, 7),
                                            self.workbook.datemode
                                        )
                        current_trip_time = time(*temp_trip_time[3:])
                        current_trip = self.sheet.cell_value(trip_offset, 4)

                else:
                    break

        num_clients = self.get_num_clients(trip_start, trip_offset)

        return (desired_trip + ' - ' + str(trip_time), num_clients, trip_offset)


    def get_num_clients(self, trip_start, trip_offset):
        """Sums the number of clients booked in each group for the total number
        of clients

        Parameters
        ----------
        trip_start : int
            An integer representing the row number where the data for the
            current trip starts
        trip_offset : int
            An integer representing the row number where the data for the
            next trip starts

        Returns
        ------
        int
            An integer representation of the number of clients booked onto the
            current trip
        """

        num_clients = 0

        for x in range(trip_start, trip_offset):
            num_clients += self.sheet.cell_value(x, 8)
            x+= 1


        return num_clients

import xlrd
from datetime import time
import datetime

class excel_scraper:

    def __init__(self, new_file_path):
        self.file_path = new_file_path
        self.workbook = xlrd.open_workbook(self.file_path)
        self.sheet = self.workbook.sheet_by_index(0)
        self.num_rows = self.sheet.nrows
        print("workbook opened")

################################################################################


    def get_first_date(self):
        date = datetime.datetime(
                    *xlrd.xldate_as_tuple(
                        self.sheet.cell_value(2, 5),
                        self.workbook.datemode
                    )
                )

        first_date = date.date().isoformat()

        return first_date

################################################################################


    def get_num_days(self):

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

        else:

            print("doesn't work")

        return num_days

################################################################################
    #return a dictionary with each trip and its corresponding start value

    def get_day(self, current_date):

        print("Reading trip data for ",current_date)

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
        #print("new offset: "+str(offset))
        temp_tuple = self.getTrip(offset)
        trips[temp_tuple[0]] = temp_tuple[1]

        current_date = self.sheet.cell_value(offset, 5)
        desired_date = self.sheet.cell_value(offset, 5)

        while current_date == desired_date:
            current_date = self.sheet.cell_value(temp_tuple[2]+1, 5)
            if(current_date == desired_date):
                temp_tuple = self.getTrip(temp_tuple[2])
                trips[temp_tuple[0]] = temp_tuple[1]

        print("###################################################################")
        for x in trips:
            print (x, trips[x])
        print("###################################################################")

        return trips

################################################################################


    def get_new_offset(self, current_date):

        default_offset = 2;
        new_date = datetime.datetime(
                        *xlrd.xldate_as_tuple(
                            self.sheet.cell_value(default_offset, 5),
                            self.workbook.datemode
                        )
                    )

        date = date = new_date.date().isoformat()

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

################################################################################


    def getTrip(self, offset):

        trip_start = offset
        #print('trip start',trip_start)
        trip_offset = offset

        trip_time = xlrd.xldate_as_tuple(
                        self.sheet.cell_value(trip_offset, 7),
                        self.workbook.datemode
                    )

        #print("trip time", trip_time)


        trip_time_date = datetime.datetime(
                            *xlrd.xldate_as_tuple(
                                self.sheet.cell_value(trip_offset, 5),
                                self.workbook.datemode
                            )
                        )

        date = trip_time_date.date().isoformat()
        #print("time", date)
        trip_time = time(*trip_time[3:])
        current_trip_time = trip_time
        #print("CURRENT TIME original", current_trip_time)
        current_trip = self.sheet.cell_value(trip_start, 4)
        desired_trip = self.sheet.cell_value(trip_start, 4)

        while current_trip == desired_trip:

            #print("current time, desired time", current_trip_time, trip_time)
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

        #print('total num clients', num_clients)

        num_clients = self.getNumClients(trip_start, trip_offset)

        return (desired_trip + ' - ' + str(trip_time), num_clients, trip_offset)

################################################################################


    def getNumClients(self, trip_start, trip_offset):
        #print("start, offset", trip_start, trip_offset)

        num_clients = 0

        for x in range(trip_start, trip_offset):

            num_clients += self.sheet.cell_value(x, 8)
            x+= 1
            #print('clients',trip_start,num_clients,x)
        #print('returning',num_clients)

        return num_clients

################################################################################

#scraper = excel_scraper("C:\\Users\\kayle\\Desktop\\Gui\\Python Files\\data2.xlsx")
#print(scraper.get_num_days())

    #trips = get_day('2018-07-25')
    #
    #for x in trips:
    #    print (x, trips[x])

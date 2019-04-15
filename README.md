# GuideScheduleSoftware
 
Takes an excel file downloaded from our booking system as input and extracts the necessary data to generate work schedules for raft guides and shuttle drivers at a whitewater rafting company

This project has a user-friendly interface built using Qt and PySide and displays all relevant data concerning schedules, as well as the capabilities and tallies of trips worked for each staff member.

The schedules are created by determining which staff member has the highest priority for each work role on each trip. Calculations produce a set priority values for each staff member, where each value is attached a work role on a certain trip. The staff member with the lowest priority value is the top choice for that role.

The priorities for the guides are calculated according to the following equation:


![](read_me_img/guide_priority_equation.png)


Where

    Tg: Number of times the guide has worked any role on this trip
 
    Ta: Number of times all guides have worked any role on this trip
 
    Rg: Number of times the guide has worked this role on any trip
 
    Ra: Number of times all guides have worked this role on any trip
 
    c(i): Whether or not the guide is allowed to work this role on this trip (1 or 0)
 
    w(i): The weight value assigned to this trip
    
    n: The number of trip types
    
    m: The number of role types 


The priorities for the drivers are calculated according to the following equation:


![](read_me_img/driver_priority_equation.png)


Where

    Tds: Number of times the driver has worked on this trip throughout the summer
 
    Tas: Number of times all drivers have worked on this trip throughout the summer
 
    Tdp: Number of times the driver has worked on this trip since the start of the most recent period
 
    Tap: Number of times all drivers have worked on this trip since the start of the most recent period
 
    c(i): Whether or not the driver is allowed to work this trip (1 or 0)
 
    w(i): The weight value assigned to this trip
    
    n: The number of trip types
    
    x: The ID number of the trip being scheduled

After the priorities have been calculated, program logic is used to refine the ordering further based on additional factors such as ensuring each trip has at least one staff member with a Class 4 driver's license, and ranking the drivers by their seniority levels for each trip.

import re
import math


def get_day_key(day):
    match day.capitalize():
        case 'Monday':
            return 1
        case 'Tuesday':
            return 2
        case 'Wednesday':
            return 3
        case 'Thursday':
            return 4
        case 'Friday':
            return 5
        case 'Saturday':
            return 6
        case 'Sunday':
            return 7


def add_time(start, duration, day=None):
    daysofweek = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
                  4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    minutesregex = ''
    for i in range(6):
        minutesregex = minutesregex + \
            str(i) + "[0-9]" + ("|" if i != 5 else "")

    if not re.search('^(0{0,1}[0-9]|1[0-2]):('+minutesregex+')\s+(AM|PM)', start):
        return "strat time should be in the 12-hour clock format (ending in AM or PM)."
    if not re.search('^\d+:('+minutesregex + ')', duration):
        return "The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number."

    # framentation if start and duration arguments
    framgmentss = start.split()
    framgmentsd = duration.split(":")
    ending = framgmentss[1]
    hoursminutes = framgmentss[0].split(":")
    hourss = hoursminutes[0]
    minutess = hoursminutes[1]
    hoursd = framgmentsd[0]
    minutesd = framgmentsd[1]

    # calculations
    convertion = (int(hoursd) + (int(minutesd)+int(minutess))/60) % 12

    addHours = int(convertion) + \
        int(math.ceil(float(math.modf(convertion)[0])*60)/60)
    
    
    newminutes = int((int(minutesd)+int(minutess)) % 60)
    newhours = int((int(hourss) + int(hoursd) +
                   (int(minutesd)+int(minutess))/60) % 12)

    newdays = ((int(hourss) + int(hoursd) +
                          (int(minutesd)+int(minutess))/60)) / 24

    newdays = 0 if newdays <= 1 else  round(newdays)

    conventionAMPM = ending if addHours + \
        int(hourss) < 12 and (newdays % 2 == 0 or newdays == 1) else ('PM' if ending == 'AM' else ('AM' if ending == 'PM' else ending))
    
    newdays = (1 if newdays == 0 and  conventionAMPM == 'AM' and conventionAMPM!= ending else newdays)

    # some formating
    newhours = int(12) if newhours == 0 else newhours

    new_time = str(newhours) + ":" + str(newminutes).zfill(2) +" " +conventionAMPM

    # for days :
    
    if day is not None:
         dayindex = (get_day_key(day) + newdays) % 7
         new_time = new_time +", "+ daysofweek.get((7 if dayindex == 0 else dayindex))  + ( "" if newdays ==0 else (" (next day)" if newdays == 1 else " (" + str(newdays) +" days later)" ))
    else :
        new_time = new_time + ( "" if newdays ==0 else (" (next day)" if newdays == 1 else " (" + str(newdays) +" days later)" ))

    return new_time 


    # return new_time
add_time("2:59 AM", "24:00","saturDay")

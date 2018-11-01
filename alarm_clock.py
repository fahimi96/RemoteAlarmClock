
# Setup
ampm = 0;
alarm = 0;
alarm_hour = 0;
alarm_minute = 0;

update()

def update:
    while(1):
        datetime_hour = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute
        hour = datetime_hour
        
        if datetime_hour < 12:
            ampm = 0
        else
            ampm = 1

        if datetime_hour > 12:
            hour = datetime_hour - 12

        if alarm == 1 and alarm_hour == datetime_hour and alarm_minute == minute:
            alarm_on()

        set_7seg(hour, minute)


def alarm_on():
    # code for turning alarm sound on
    return 0

def alarm_off():
    # code for turning alarm sound off
    return 0

def set_alarm_hour():
    if alarm_hour == 23:
        alarm_hour = 0
    else
        alarm_hour = alarm_hour + 1

def set_alarm_minute():
    if alarm_minute == 59:
        alarm_minute = 0
    else
        alarm_minute = alarm_minute + 1

def show_alarm():
    a_hour = alarm_hour
    if alarm_hour < 12:
        ampm = 0
    else
        ampm = 1

    if alarm_hour > 12:
        a_hour = alarm_hour - 12
    set_7seg(a_hour, alarm_minute)

def set_7seg(hour, minute):
    # code for setting seven segment display
    return 0

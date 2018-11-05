
from Adafruit_LED_Backpack import SevenSegment

# Setup
ampm = 0;
alarm = 0;
alarm_hour = 0;
alarm_minute = 0;
segment = SevenSegment.SevenSegment(address=0x70)
segment.begin()

update()

def update():
    while(1):
        datetime_hour = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute
        hour = datetime_hour
        
        if datetime_hour < 12:
            ampm = 0
        else:
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
    else:
        alarm_hour = alarm_hour + 1

def set_alarm_minute():
    if alarm_minute == 59:
        alarm_minute = 0
    else:
        alarm_minute = alarm_minute + 1

def show_alarm():
    a_hour = alarm_hour
    if alarm_hour < 12:
        ampm = 0
    else:
        ampm = 1

    if alarm_hour > 12:
        a_hour = alarm_hour - 12
    set_7seg(a_hour, alarm_minute)

def set_7seg(hour, minute):
    segment.clear()
    # Set hours
    segment.set_digit(0, int(hour / 10))     # Tens
    segment.set_digit(1, hour % 10)          # Ones
    # Set minutes
    segment.set_digit(2, int(minute / 10))   # Tens
    segment.set_digit(3, minute % 10)        # Ones
    # Toggle colon
    segment.set_colon(second % 2)              # Toggle colon at 1Hz

    # Write the display buffer to the hardware.  This must be called to
    # update the actual display LEDs.
    segment.write_display()

    # Wait a quarter second (less than 1 second to prevent colon blinking getting$
    time.sleep(0.25)
    return 0

import Adafruit_BBIO.GPIO as GPIO
import time
import datetime
import os
from Adafruit_LED_Backpack import SevenSegment

# Setup
ampm = 0;
alarm = 0;
alarm_hour = 0;
alarm_minute = 0;
segment = SevenSegment.SevenSegment(address=0x70, busnum=2)
segment.begin()

buttonSnooze= "P9_21"  #
buttonSetAlarm="P9_22"
buttonHour= "P9_23"  # 
buttonMinute="P9_24"

GPIO.setup(buttonSnooze, GPIO.IN)
GPIO.setup(buttonSetAlarm, GPIO.IN)
GPIO.setup(buttonHour, GPIO.IN)
GPIO.setup(buttonMinute, GPIO.IN)


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

        if GPIO.input("P9_22"):
            set_7seg(alarm_hour, alarm_minute)
        else:
            set_7seg(hour, minute)



def alarm_on():
    os.system('mpg123 phantom_words_ex1.mp3')
    alarm = 0
    return 0

def alarm_off(channel):
    os.system('pidof mpg123 | xargs kill -9')
    alarm = 0
    return 0

def set_alarm_hour(channel):
    global alarm_hour
    if alarm_hour == 23:
        alarm_hour = 0
    else:
        alarm_hour = alarm_hour + 1

def set_alarm_minute(channel):
    global alarm_minute
    if alarm_minute == 59:
        alarm_minute = 0
    else:
        alarm_minute = alarm_minute + 1


def set_7seg(hour, minute):
    segment.clear()
    # Set hours
    segment.set_digit(0, int(hour / 10))     # Tens
    segment.set_digit(1, hour % 10)          # Ones
    # Set minutes
    segment.set_digit(2, int(minute / 10))   # Tens
    segment.set_digit(3, minute % 10)        # Ones
    # Toggle colon
    segment.set_colon(datetime.datetime.now().second % 2)              # Toggle colon at 1Hz

    # Write the display buffer to the hardware.  This must be called to
    # update the actual display LEDs.
    segment.write_display()

    # Wait a quarter second (less than 1 second to prevent colon blinking getting$
    time.sleep(0.25)
    return 0

GPIO.add_event_detect(buttonSnooze, GPIO.FALLING, callback=alarm_off, bouncetime=200) # RISING, FALLING$
GPIO.add_event_detect(buttonHour, GPIO.FALLING, callback=set_alarm_hour, bouncetime=200) # RISING, FALLING$
GPIO.add_event_detect(buttonMinute, GPIO.FALLING, callback=set_alarm_minute, bouncetime=200)


update()

import Adafruit_BBIO.GPIO as GPIO
import time
import datetime
import os
from Adafruit_LED_Backpack import SevenSegment

# Setup
ampm = 0
alarm = 1
alarm_hour = 0
alarm_minute = 0
segment = SevenSegment.SevenSegment(address=0x70, busnum=2)
segment.begin()

buttonSnooze= "P9_21"  #
buttonSetAlarm="P9_22"
buttonHour= "P9_23"  # 
buttonMinute="P9_24"
buttonAlarmToggle="P9_25"

LEDalarmOnOff="P9_26"
LEDampm="P9_27"

GPIO.setup(buttonSnooze, GPIO.IN)
GPIO.setup(buttonSetAlarm, GPIO.IN)
GPIO.setup(buttonHour, GPIO.IN)
GPIO.setup(buttonMinute, GPIO.IN)
GPIO.setup(buttonAlarmToggle, GPIO.IN)
GPIO.setup(LEDalarmOnOff, GPIO.OUT)
GPIO.setup(LEDampm, GPIO.OUT)


GPIO.output(LEDalarmOnOff, alarm)

def update():
    global ampm
    global alarm
    global alarm_hour
    global alarm_minute
    while(1):
        datetime_hour = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute
        hour = datetime_hour
        alarm_hour_ampm = alarm_hour

        if datetime_hour > 12:
            hour = datetime_hour - 12
        if alarm_hour > 12:
            alarm_hour_ampm = alarm_hour - 12

        if alarm == 1 and alarm_hour == datetime_hour and alarm_minute == minute:
            alarm_on()
            alarm = 0
            GPIO.output(LEDalarmOnOff, alarm)

        if GPIO.input("P9_22"):
            set_7seg(alarm_hour_ampm, alarm_minute)
            if alarm_hour < 12:
                ampm = 0
            else:
                ampm = 1
        else:
            set_7seg(hour, minute)
            if datetime_hour < 12:
                ampm = 0
            else:
                ampm = 1
        GPIO.output(LEDampm, ampm)



def alarm_on():
    os.system('cvlc --no-video https://www.youtube.com/watch?v=nPRHumwZfk4')
    return 0

def alarm_off(channel):
    os.system('^C')
    return 0

def alarm_toggle(channel):
    global alarm
    if alarm == 1:
        alarm = 0
    else:
        alarm = 1
    GPIO.output(LEDalarmOnOff, alarm)

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
GPIO.add_event_detect(buttonAlarmToggle, GPIO.FALLING, callback=alarm_toggle, bouncetime=200)


update()

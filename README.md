# RemoteAlarmClock
Created by Brian Jennings and Manoj Kurapati

## Running Program
1. `Bone:~/RemoteAlarmClock/$ ./install.sh`
2. Follow Bluetooth instructions below
3. `Bone:~/RemoteAlarmClock/$ python alarm_clock.py`

## Setting up Bluetooth
1. `Bone:~/RemoteAlarmClock/$ pulseaudio --start`
2. `Bone:~/RemoteAlarmClock/$ bluetoothctl`
3. `[Bluetooth] scan on`
4. Search for your Bluetooth Device Address
5. `[Bluetooth] pair (insert deive Address here)`
6. `[Bluetooth] tust (insert deive Address here)`
7. `[Bluetooth] connect (insert deive Address here)`
8. `[Device name] exit`

If the connection is giving you issues, try `pulseaudio -k` to kill it and `pulseaudio --start` to restart it.  Then open the Blluetooth menu to try and connect again.

## Changing Youtube Video
The video that is played for the alarm can be changed by opening alarm_clock.py and editing line 82 to be the correct video URL.
Line 82 is shown below.

```python
#Running cvlc from console for youtube.  Enter desired youtube link here.
    proc = subprocess.Popen(['cvlc', '--no-video', 'https://www.youtube.com/watch?v=nPRHumwZfk4'])
```

## More information
A complete description of this project and wiring instructions can be found on our [Wiki](https://elinux.org/ECE497_Project:_Alarm_with_Remote_Speaker) or on our [Hackster.io](https://www.hackster.io/manoj-kurapati/ece497-project-alarm-with-remote-speaker-5eae5d)

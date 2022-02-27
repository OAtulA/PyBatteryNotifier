import psutil
import os
from playsound import playsound
import time

def percent_check():
    # returns a tuple
    battery = psutil.sensors_percent()
    percent = battery.percent

    charging= battery.power_plugged()

    # Checking percent
    if percent <= 20 and not charging:
        os.system("notify-send '" + 'percent%' + "' '" + percent + "'")
        playsound('sounds/mixkit-wrong-answer-fail-notification-946.wav')
    elif percent == 30:
        os.system("notify-send '" + 'percent%' + "' '" + percent + "'")
        playsound('sounds/mixkit-bell-notification-933.wav')
    elif percent == 40 and :
        os.system("notify-send '" + 'percent%' + "' '" + percent + "'")
        playsound('sounds/mixkit-bell-notification-933.wav')
    elif percent >=93 and charging:
        os.system("notify-send '" + 'percent%' + "' '" + percent + "'")
        playsound('sounds/mixkit-bell-notification-933.wav')
        playsound('sounds/mixkit-melodical-flute-music-notification-2310.wav')

while True:
    percent_check()

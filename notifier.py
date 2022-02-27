import psutil
import os
from playsound import playsound
import time

def percent_check():
    # returns a tuple
    battery = psutil.sensors_battery()
    percent = battery.percent

    charging= battery.power_plugged

    # Checking percent
    if percent <= 20:

        percent = str(percent)
        percent= percent[:2]
        if charging:
            os.system("notify-send '" +' ' + '\U0001F979' + 'percent%' + "' '" + percent + "'")
            playsound('sounds/mixkit-melodical-flute-music-notification-2310.wav')
            time.sleep(120)
        else:
            percent = str(percent)
            percent= percent[:2]
            os.system("notify-send '" +' ' + '\U0001F97A' + 'percent%' + "' '" + percent + "'")
            playsound('sounds/mixkit-wrong-answer-fail-notification-946.wav')
            time.sleep(180)        
    elif percent == 30:
        percent = str(percent)
        percent= percent[:2]
        os.system("notify-send '" + ' '+ '\U0001F645' + 'percent%' + "' '" + percent + "'")
        playsound('sounds/mixkit-bell-notification-933.wav')
        time.sleep(300)
    elif percent == 40 :
        percent = str(percent)
        percent= percent[:2]
        os.system("notify-send '" + ' '+ '\U0001F481' + 'percent%' + "' '" + percent + "'")
        playsound('sounds/mixkit-bell-notification-933.wav')
        time.sleep(300)
    elif percent >=93 and charging:
        percent = str(percent)
        percent= percent[:2]
        os.system("notify-send '"+ ' '+ '\U0001F525' + 'percent%' + "' '" + percent + "'")
        playsound('sounds/mixkit-bell-notification-933.wav')
        playsound('sounds/mixkit-happy-bells-notification-937.wav')
        time.sleep(120)
    else:
        time.sleep(120)
    
while True:
    percent_check()    


'''

To Add notifier to startup apps.
See the README.md file
'''

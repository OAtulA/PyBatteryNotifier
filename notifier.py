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
            playsound('Music/BatteryNotifySound/mixkit-melodical-flute-music-notification-2310.wav')
            time.sleep(120)        
        else:
            percent = str(percent)
            percent= percent[:2]
            os.system("notify-send '" +' ' + '\U0001F97A' + 'percent%' + "' '" + percent + "'")
            playsound('Music/BatteryNotifySound/mixkit-wrong-answer-fail-notification-946.wav')
            time.sleep(180)        
    elif percent >= 30 and percent <= 33 and not charging:
        percent = str(percent)
        percent= percent[:2]
        os.system("notify-send '" + ' '+ '\U0001F645' + 'percent%' + "' '" + percent + "'")
        playsound('Music/BatteryNotifySound/mixkit-bell-notification-933.wav')
        time.sleep(300)
    elif percent >= 40 and percent <= 43 and not charging:
        percent = str(percent)
        percent= percent[:2]
        os.system("notify-send '" + ' '+ '\U0001F481' + 'percent%' + "' '" + percent + "'")
        playsound('Music/BatteryNotifySound/mixkit-bell-notification-933.wav')
        time.sleep(300)
    elif percent >=93 and charging:
        percent = str(percent)
        percent= percent[:2]
        os.system("notify-send '"+ ' '+ '\U0001F525' + 'percent%' + "' '" + percent + "'")
        playsound('Music/BatteryNotifySound/mixkit-bell-notification-933.wav')
        playsound('Music/BatteryNotifySound/mixkit-happy-bells-notification-937.wav')
        time.sleep(75)        
    else: # To check every 2 minutes
        time.sleep(120)
    
while True:
    percent_check()    


'''

To Add notifier to startup apps.
See the README.md file
'''

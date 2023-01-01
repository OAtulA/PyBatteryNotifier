#!/bin/bash

#Installing the required python libraries.
pip install psutil==5.5.1
pip install playsound==1.3.0

pip3 install psutil==5.5.1
pip3 install playsound==1.3.0  

#To move the sound files to their correct location to be played.
mkdir ~/Music/BatteryNotifySound
cp BatteryNotifySound/*.wav ~/Music/BatteryNotifySound
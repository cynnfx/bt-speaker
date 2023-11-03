#!/bin/python

import os
import RPi.GPIO as GPIO
import time
import subprocess

# Use the Broadcom SOC Pin numbers
# Setup the Pin with Internal pullups enabled and PIN in reading mode.
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Our function on what to do when the button is pressed
def service_restart(channel):
    status = os.system('sudo systemctl is-active --quiet bt_speaker.service')
    if status == 0:
        cmd = "sudo systemctl stop bt_speaker.service"
        subprocess.call(["ogg123 /usr/share/sounds/freedesktop/stereo/service-logout.oga"], shell=True)
    else:
        cmd = "sudo systemctl start bt_speaker.service"
        subprocess.call(["ogg123 /usr/share/sounds/freedesktop/stereo/service-login.oga"], shell=True)
    subprocess.call([cmd], shell=True)
    # time.sleep(2)

# Add our function to execute when the button pressed event happens
GPIO.add_event_detect(2, GPIO.FALLING, callback = service_restart, bouncetime = 5000)

# Now wait!
while 1:
    time.sleep(1)
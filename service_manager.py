#!/bin/python

import os
import RPi.GPIO as GPIO
import time
import subprocess
import configparser

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))

config = configparser.ConfigParser()
config.read(SCRIPT_PATH + '/config.ini.default')
config.read('/etc/bt_speaker/config.ini')
BT_NAME = config.get('bluez', 'bt_name')

def start_service():
    subprocess.call(["ogg123 /usr/share/sounds/freedesktop/stereo/service-login.oga"], shell=True)
    subprocess.call(["systemctl start bt_speaker.service"], shell=True)
def stop_service():
    subprocess.call(["systemctl stop bt_speaker.service"], shell=True)
    subprocess.call(["ogg123 /usr/share/sounds/freedesktop/stereo/service-logout.oga"], shell=True)
def init_bt():
    subprocess.call(["ogg123 /usr/share/sounds/freedesktop/stereo/service-login.oga"], shell=True)
    subprocess.call([f"bluetoothctl system-alias '{BT_NAME}'"], shell=True)
    subprocess.call(["systemctl restart bt_speaker.service"], shell=True)


def button_callback(channel):
    status = os.system('systemctl is-active --quiet bt_speaker.service')
    if status == 0: start_service()
    else: stop_service()

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 7 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(7,GPIO.RISING,callback=button_callback, bouncetime=5000) # Setup event on pin 7 rising edge
init_bt()

while 1: time.sleep(1)
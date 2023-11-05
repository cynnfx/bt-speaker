#!/bin/python3

import os
import RPi.GPIO as GPIO
import time
import subprocess
import configparser

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
BT_NAME = "BluetoothSpeaker"
BTN_PIN = 7
SOUND_WELCOME = "/usr/share/sounds/freedesktop/stereo/service-login.oga"
SOUND_OFF = "/usr/share/sounds/freedesktop/stereo/service-logout.oga"

status = 0
config = configparser.ConfigParser()
config.read(SCRIPT_PATH + '/config.ini.default')
config.read('/etc/bt_speaker/config.ini')
config.read('/boot/bt_config.ini')

if config.has_section('bt_addition'):
    BT_NAME = config.get('bt_addition', 'bt_name', fallback=BT_NAME)
    SOUND_WELCOME = config.get('bt_addition', 'sound_welcome', fallback=SOUND_WELCOME)
    SOUND_OFF = config.get('bt_addition', 'sound_off', fallback=SOUND_OFF)

def start_service():
    GPIO.remove_event_detect(BTN_PIN)
    subprocess.call([f"ogg123 --quiet {SOUND_WELCOME}"], shell=True, stdin=None, stdout=None, stderr=None)
    subprocess.call(["systemctl start bt_speaker.service"], shell=True, stdin=None, stdout=None, stderr=None)
    GPIO.add_event_detect(BTN_PIN,GPIO.BOTH,callback=button_callback, bouncetime=200)

def stop_service():
    GPIO.remove_event_detect(BTN_PIN)
    subprocess.call(["systemctl stop bt_speaker.service"], shell=True, stdin=None, stdout=None, stderr=None)
    subprocess.call([f"ogg123 --quiet {SOUND_OFF}"], shell=True, stdin=None, stdout=None, stderr=None)
    GPIO.add_event_detect(BTN_PIN,GPIO.BOTH,callback=button_callback, bouncetime=200)

def init_bt():
    global status
    subprocess.call([f"ogg123 --quiet {SOUND_WELCOME}"], shell=True, stdin=None, stdout=None, stderr=None)
    subprocess.call([f"bluetoothctl system-alias '{BT_NAME}'"], shell=True, stdin=None, stdout=None, stderr=None)
    subprocess.call(["systemctl restart bt_speaker.service"], shell=True, stdin=None, stdout=None, stderr=None)
    status = 1

def button_callback(channel):
    global status
    status = 0 if status == 1 else 1
    if status == 0: stop_service()
    else: start_service()

init_bt()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin BTN_PIN to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(BTN_PIN,GPIO.BOTH,callback=button_callback, bouncetime=200)

while 1: time.sleep(1)
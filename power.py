#!/usr/bin/env python

import time

import RPi.GPIO as GPIO
from database import update_relay_DB

pin = 17
#from database import update_relay_DB 
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(17, GPIO.OUT)
#print(GPIO.gpio_function(17))
#time.sleep(5)
#GPIO.setup(17, GPIO.IN)
#print(GPIO.gpio_function(17))
#time.sleep(5)
#GPIO.setup(17, GPIO.OUT)
#print(GPIO.gpio_function(17))
#time.sleep(5)
#GPIO.cleanup()

def update_relay(state):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    update_relay_DB(state)

def get_relay_status():
    GPIO.setmode(GPIO.BCM)
    return GPIO.gpio_function(pin)
    

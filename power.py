#!/usr/bin/env python

import time

import RPi.GPIO as GPIO

print("hih")
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, GPIO.HIGH)

time.sleep(5)

print("low")
GPIO.output(17, GPIO.LOW)

time.sleep(5)

print("high")
GPIO.output(17, GPIO.HIGH)

time.sleep(5)

print ("off")
GPIO.cleanup()


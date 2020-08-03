#!/usr/bin/env python

import time

import RPi.GPIO as GPIO

print("set")
GPIO.setmode(GPIO.BCM)
time.sleep(5)

print("set out")
GPIO.setup(17, GPIO.OUT)
time.sleep(5)

print("low")
GPIO.setup(17, GPIO.IN)
time.sleep(5)

print("high")
GPIO.setup(17, GPIO.OUT)
time.sleep(5)

print("clean")
GPIO.cleanup()
time.sleep(5)

print("end")

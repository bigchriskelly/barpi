#!/usr/bin/python
#--------------------------------------
#
#
#
#
#--------------------------------------
import time
import RPi.GPIO as GPIO
import time,sys, datetime


GPIO.setmode(GPIO.BCM)
inpt = 26
GPIO.setup(inpt,GPIO.IN)

while True:
	new_input = GPIO.input(inpt)
	print("Time is: " + time.asctime(time.localtime()) + "  Meter reading is: " + str(new_input))
	time.sleep(1)

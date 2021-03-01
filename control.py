#!/usr/bin/python
#--------------------------------------
#
#
#
#
#--------------------------------------
import time

from temp import record_temp
from database import get_goal_temp
from database import get_wiggle_temp
from database import get_is_crash
from database import get_keg_temp
#from weight import  record_weight
#from lcd import update_lcd
from power import update_relay
from power import get_relay_status
from lcd1 import initial_lcd_load as initial_lcd_load1
from lcd2 import initial_lcd_load as initial_lcd_load2
from lcd1 import update_lcd_abv as update_lcd_abv1
from lcd2 import update_lcd_abv as update_lcd_abv2
# run a loop every 300s
# log temp to db
# log weight to db
# update LCD
# update relay

def are_we_at_the_right_temp():
    keg1_temp = get_keg_temp(1)
    keg2_temp = get_keg_temp(2)
    keg_goal_temp = get_goal_temp()
    keg_temp_wiggle = get_wiggle_temp()

    if get_is_crash():
        #crashing temp#
	print("crash")
        return 1
    
    elif (keg1_temp >= (keg_goal_temp + keg_temp_wiggle)) or (keg2_temp >= (keg_goal_temp + keg_temp_wiggle)):
        #either keg is above upper range
	print keg1_temp, keg2_temp, keg_goal_temp, keg_temp_wiggle
	print("at least one keg is too warm")
        return 1
    
    elif (keg1_temp <= (keg_goal_temp - keg_temp_wiggle)) and (keg2_temp <= (keg_goal_temp - keg_temp_wiggle)): 
        #both are bellow lower range
	print("both are too cold")
        return 0

    #elif (keg1_temp in range((keg_goal_temp - keg_temp_wiggle), (keg_goal_temp + keg_temp_wiggle))) or (keg2_temp in range((keggoal_temp - keg_temp_wiggle), (keg_goal_temp + keg_temp_wiggle))):
    elif (((keg1_temp >= (keg_goal_temp - keg_temp_wiggle)) and (keg1_temp <= (keg_goal_temp + keg_temp_wiggle))) or ((keg2_temp >= (keg_goal_temp - keg_temp_wiggle)) and (keg2_temp <= (keg_goal_temp + keg_temp_wiggle)))):
	print("at least one keg is in range")
	#if one is in range
        if get_relay_status():
	    print("...and relay is running")
            #and the relaty is running
            return 1
        else:
	    print("...and relat isn't running")
            return 0
    else:
        #something is wonky...
        return 1


def main_loop():
    temp = ["", ""]
    sensor_index = 0
    initial_lcd_load1()
    initial_lcd_load2()
    while True:
    
        #measure and record the temp
        if sensor_index == 0:
            temp[sensor_index] = record_temp(sensor_index)
            sensor_index = 1
            temp[sensor_index] = record_temp(sensor_index)
        else:
            sensor_index = 0
            if are_we_at_the_right_temp():
                update_relay(1)
            update_lcd_abv1(temp[0])
            update_lcd_abv2(temp[1])
        time.sleep(10)


#update_relay(1)
#time.sleep(3)
#update_relay(0)
#time.sleep(3)
#update_relay(1)

#!/usr/bin/python
#--------------------------------------
#
#
#
#
#--------------------------------------
import time

from temp import record_temp
from database import get_tempGoal
#from weight import  record_weight
#from lcd import update_lcd
#from power import update_relay
# run a loop every 300s
# log temp to db
# log weight to db
# update LCD
# update relay

temp = record_temp()

#update_relay(1)
#time.sleep(3)
#update_relay(0)
#time.sleep(3)
#update_relay(1)

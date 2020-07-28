#!/usr/bin/python
#--------------------------------------
#
#
#
#
#--------------------------------------
from temp import record_temp
from weight import  record_weight
from lcd import update_lcd
from power import update_relay

# run a loop every 300s
# log temp to db
# log weight to db
# update LCD
# update relay

while true:
    record_temp()
    record_weight()
    update_lcd()
    update_relay()
    wait(300s)

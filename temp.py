import glob
import time
from database import update_temp

sensor_index = 0
base_dir = '/sys/bus/w1/devices/'
device_postfix = '/w1_slave'

def read_temp_raw(device_file):
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp(sensor_index):
    device_folder = glob.glob(base_dir + '28*')[sensor_index]
    device_file = device_folder + device_postfix
    lines = read_temp_raw(device_file)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_string = "Keg " + str(sensor_index + 1) + ": " + str(temp_c)
        return temp_c

def record_temp(sensor_index):
    base_dir = '/sys/bus/w1/devices/'
    device_postfix = '/w1_slave'
    #print(read_temp(sensor_index))
    temp = read_temp(sensor_index)
    update_temp (sensor_index, temp) 
    return temp 

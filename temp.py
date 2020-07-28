import glob
import time

bus_index = 0
#base_dir = '/sys/bus/w1/devices/'
#device_folder = glob.glob(base_dir + '28*')[bus_index]
#device_file = device_folder + '/w1_slave'

def read_temp_raw(device_file):
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[bus_index]
    device_file = device_folder + '/w1_slave'
    lines = read_temp_raw(device_file)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_formatted = "sensor " + str(bus_index + 1) + ": "  + str(temp_c)
        return temp_formatted

while True:
    print(read_temp())
    time.sleep(1)
    if bus_index == 1:
        bus_index = 0
    else:
        bus_index = 1

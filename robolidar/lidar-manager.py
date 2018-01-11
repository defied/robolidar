#!/usr/bin/python3
import serial
import argparse
from lib import serial_control
import logging
import time
import sys

# Options
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--port', metavar='', help='Serial device port', default='/dev/serial')
parser.add_argument('-b', '--baud', metavar='', type=int, help='Baudrate', default=115200)
parser.add_argument('-v', '--version', metavar='', help='Version')
parser.add_argument('-ms', '--set_motor', metavar='', type=int, help='Adjust Motor Speed [1-10]', choices=list(range(1,11)), default=5)
parser.add_argument('-lr', '--set_lidar', metavar='', type=int, help='Adjust LiDAR Sample Rate [1,2,3]', choices=list(range(1,4)), default=2)
args = parser.parse_args()

# Logging
date_time = time.strftime('%Y-%m-%d-%H:%M:%S_')
StatFile = 'lidar-manager_{}.log'.format(date_time)
# StatFile = '/var/log/lidar-manager_{}.log'.format(date_time)
LOG_FILENAME = StatFile
logging.getLogger("paramiko").setLevel(logging.WARNING)
logging.getLogger("MyLogger").setLevel(logging.DEBUG)
logging.basicConfig(filename=StatFile, level=logging.DEBUG)
logging.debug('Beginning Logging.')
statLog = logging

def serial_connect(console_port, baud_rate):
    # Connection Creation
    try:
        ser = serial_control.Serialcontrol()
        ser.connect(console_port, baud_rate)
    except:
        ser = 'Something broke in Serial.'
    return ser

def display_info():
    # Print IV, LIm MI, IV, ID
    info={}
    info[version] = 'Version: {}'.format(lidar.send('IV','')[1])
    info[motor] = 'Motor: {}'.format(lidar.send('MI','')[1])
    info[lidar] = 'Lidar: {}'.format(lidar.send('LI','')[1])
    info[device] = 'Device: {}'.format(lidar.send('ID','')[1])
    return info

def set_motor_speed(speed):
    set_speed = speed
    return set_speed

def set_lidar_speed(speed):
    set_speed = speed
    return set_speed

def get_lidar_ready():
    return

# Connect to lidar:
lidar = serial_connect(args.port, args.baud)

# Validate connection:
if 'broke' in lidar:
    print('Failed to connect to lidar.\nReason: {}'.format(lidar))
    statLog.debug('Failed to connect to lidar: {}'.format(lidar))
    sys.exit(165)

if args.version:
    info = display_info()
    for i in info:
        print(i)

if args.set_motor:
    set_motor_speed(args.set_motor)


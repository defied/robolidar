#!/usr/bin/python3
__author__ = 'Dafydd'
#
import argparse
import serial
import logging
import time
import sys
from networktables import NetworkTables

# Variables
host = '10.25.57.2'

# Options
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--port', metavar='', help='set serial device port', default='/dev/serial')
parser.add_argument('-b', '--baud', metavar='', type=int, help='set baudrate', default=115200)
parser.add_argument('-c', '--command', metavar='', help='send custom command')
parser.add_argument('-v', '--version', action="store_true", default=False)
parser.add_argument('-ms', '--set_motor', metavar='', type=int, help='adjust Motor Speed [1-10]', choices=list(range(1,11)), default=5)
parser.add_argument('-lr', '--set_lidar', metavar='', type=int, help='adjust LiDAR Sample Rate [1,2,3]', choices=list(range(1,4)), default=2)
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

# Network tables
# NetworkTables.initialize(server=host)


# lidar
def serial_connect(console_port, baud_rate):
    ''' Calls the Serial controller and creates the connection.'''
    try:
        ser = serial.Serial(console_port, baud_rate, parity=serial.PARITY_NONE, bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE, xonxoff=False, rtscts=False, dsrdtr=False)
    except:
        ser = 'Something broke in Serial.'
    return ser

def display_info():
    ''' Print IV, LIm MI, IV, ID.'''
    results = {}
    lidar.write(b"IV\r\n")
    time.sleep(1)
    results['Version'] = lidar.read(lidar.inWaiting()).decode('utf-8')
    lidar.write(b'LI\r\n')
    time.sleep(1)
    results['Resolution'] = lidar.read(lidar.inWaiting()).decode('utf-8')
    lidar.write(b'MI\r\n')
    time.sleep(1)
    results['Speed'] = lidar.read(lidar.inWaiting()).decode('utf-8')
    lidar.write(b'ID\r\n')
    time.sleep(1)
    results['ID'] = lidar.read(lidar.inWaiting()).decode('utf-8')
    return results

def set_motor_speed(motor_speed):
    ''' Set the motor speed.'''
    set_speed = motor_speed
    return set_speed

def set_lidar_speed(sample_rate):
    ''' Set the lidar Sample Rate'''
    set_speed = sample_rate
    return set_speed

def get_lidar_ready():
    ''' Make sure the lidar is ready to go before polling.'''
    return

# Connect to lidar:
print('Connecting to lidar. Setting: {} {}\r\n'.format(args.baud, args.port))
lidar = serial_connect(args.port, args.baud)

if args.command:
    ret = lidar.send('{}'.format(args.command),'')[1]
    print('Command Response: {}'.format(ret))
    sys.exit(0)

if args.version:
    info = display_info()
    for i in info:
        m = info[i]
        print(i + ": " + m)
    sys.exit(0)

if args.set_motor:
    set_motor_speed(args.set_motor)

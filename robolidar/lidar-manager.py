#!/usr/bin/python3
__author__ = 'Dafydd'
#
import argparse
from lib import serial_control
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
parser.add_argument('-c', '--commandn', metavar='', help='send custom command')
parser.add_argument('-v', '--version', metavar='', help='show version')
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
NetworkTables.initialize(server=host)


# lidar
def serial_connect(console_port, baud_rate):
    ''' Calls the Serial controller and creates the connection.'''
    try:
        ser = serial_control.Serialcontrol()
        ser.connect(console_port, baud_rate)
    except:
        ser = 'Something broke in Serial.'
    return ser

def display_info():
    ''' Print IV, LIm MI, IV, ID.'''
    info={}
    info[version] = 'Version: {}'.format(lidar.send('IV','')[1])
    info[motor] = 'Motor: {}'.format(lidar.send('MI','')[1])
    info[lidar] = 'Lidar: {}'.format(lidar.send('LI','')[1])
    info[device] = 'Device: {}'.format(lidar.send('ID','')[1])
    return info

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
lidar = serial_connect(args.port, args.baud)

# Validate connection:
if 'broke' in lidar:
    print('Failed to connect to lidar.\nReason: {}'.format(lidar))
    statLog.debug('Failed to connect to lidar: {}'.format(lidar))
    sys.exit(165)

if args.command:
    ret = lidar.send('{}'.format(args.command),'')[1]
    print('Command Response: {}'.format(ret))
    sys.exit(0)

if args.version:
    info = display_info()
    for i in info:
        print(i)

if args.set_motor:
    set_motor_speed(args.set_motor)

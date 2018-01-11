#!/usr/bin/python3
import serial
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--port', metavar='', help='Serial device port')
parser.add_argument('-b', '--baud', metavar='', type=int, help='Baudrate', default=115200)
parser.add_argument('-v', '--version', metavar='', help='Version')
parser.add_argument('-ms', '--set_motor', metavar='', type=int, help='Adjust Motor Speed [1-10]', choices=list(range(1,11)), default=5)
parser.add_argument('-lr', '--set_lidar', metavar='', type=int, help='Adjust LiDAR Sample Rate [1,2,3]', choices=list(range(1,4)), default=2)

args = parser.parse_args()

def serial_connect(console_port, baud_rate):
    # Connection Creation
    ser = serial_control.Serialcontrol()
    ser.connect(console_port, baud_rate)
    yield ser

def display_info():
    # Print IV, LIm MI, IV, ID
    info={}
    info[version] = 'version: '
    info[motor] = 'Motor: {}'.format() # Replace with serial output
    info[lidar] = 'lidar: '
    info[device] = 'device: '
    return info

def set_motor_speed(speed):
    set_speed = speed
    return set_speed

def set_lidar_speed(speed):
    set_speed = speed
    return set_speed

print(set_motor_speed(args.set_motor))

if args.version:
    display_info()

if args.set_motor:
    set_motor_speed(args.set_motor)


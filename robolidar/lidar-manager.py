#!/usr/bin/python3
import serial
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--port', help='/dev/<device serial/usb port>')
parser.add_argument('-l', '--lidar-info', help='LiDAR Information')
parser.add_argument('-m', '--motor-info', help='Motor Information')
parser.add_argument('-v', '--version', help='Version Information')
parser.add_argument('-d', '--device-info', help='Device Information')
parser.add_argument('-ms', '--set-motor-speed', help='Adjust Motor Speed [1-10]', default=5)
parser.add_argument('-lr', '--set-lidar-sr', help='Adjust LiDAR Sample Rate [1,2,3]', default=2)

args = parser.parse_args()



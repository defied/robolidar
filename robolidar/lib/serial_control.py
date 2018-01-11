#!/usr/bin/python3
__author__ = 'Dafydd'
#

import time
import serial
import logging

statLog = logging.getLogger("serial_control.py")

class Serialcontrol():
    def __init__(self):
        self.reader = None
        self.ser = None
        return None

    def connect(self, console_port, baud_rate):
        self.ser = serial.Serial(console_port, baud_rate, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE, timeout=30, xonxoff=0, rtscts=0, dsrdtr=0, exclusive=1)
        self.ser.close()
        self.ser.open()
        try:
            if self.ser.isOpen() == True:
                return self.ser
        except:
            return False

    def send(self, state_send, state_receive, sleep_timer=.1, timeout=40):
        self.ser.flushInput()
        self.ser.flushOutput()
        statLog.debug('### Running: {} ###'.format(state_send))
        start_time = time.time()
        timer = start_time + timeout
        output_log = '<<< {}'.format(state_send)
        statLog.debug(''.join([s for s in output_log.strip().splitlines(True) if s.strip()]))
        self.ser.write(str.encode(state_send))
        self.ser.write(b'\r\n')
        time.sleep(sleep_timer)
        while start_time < timer:
            time.sleep(sleep_timer)
            start_time = time.time()
            output = self.ser.readline()
            output_log = output_log + output.decode('utf-8')
            statLog.debug('>>> '.join([s for s in output.decode('utf-8').strip().splitlines(True) if s.strip()]))
            if state_receive not in output.decode('utf-8'):
                False
            elif state_receive in output.decode('utf-8'):
                statLog.debug('### Send found: {} ###'.format(state_receive))
                return True, output_log
        return False, output_log

    def send_until(self, state_send, state_receive, sleep_timer=.1, timeout=40):
        self.ser.flushInput()
        self.ser.flushOutput()
        start_time = time.time()
        timer = start_time + timeout
        output_log = ''
        time.sleep(sleep_timer)
        while state_receive not in output_log or start_time < timer:
            time.sleep(sleep_timer)
            start_time = time.time()
            self.ser.write(str.encode(state_send))
            output = self.ser.readline()
            try:
                output_log = output_log + output.decode('utf-8')
                statLog.debug('>>> '.join([s for s in output.decode('utf-8').strip().splitlines(True) if s.strip()]))
            except:
                statLog.debug('')
            if state_receive not in output.decode('utf-8'):
                False
            elif state_receive in output.decode('utf-8'):
                statLog.debug('### Return_until found: {} ###'.format(state_receive))
                return True, output_log
        return False, output_log

    def read_only(self, state_receive, sleep_timer=.1, timeout=40):
        self.ser.flushInput()
        self.ser.flushOutput()
        start_time = time.time()
        timer = start_time + timeout
        output_log = ''
        time.sleep(sleep_timer)
        while state_receive not in output_log or start_time < timer:
            start_time = time.time()
            output = self.ser.readline()
            output_log = output_log + output.decode('utf-8')
            statLog.debug('>>> '.join([s for s in output.decode('utf-8').strip().splitlines(True) if s.strip()]))
            time.sleep(sleep_timer)
            if state_receive not in output_log:
                False
            elif state_receive in output_log:
                statLog.debug('### Read_only found: {} ###'.format(state_receive))
                return True, output_log
        return False, output_log

    def return_until(self, state_receive, sleep_timer=.1, timeout=40):
        self.ser.flushInput()
        self.ser.flushOutput()
        start_time = time.time()
        timer = start_time + timeout
        output_log = ''
        time.sleep(sleep_timer)
        while state_receive not in output_log or start_time < timer:
            time.sleep(sleep_timer)
            start_time = time.time()
            self.ser.write(str.encode("\n"))
            output = self.ser.readline()
            try:
                output_log = output_log + output.decode('utf-8')
                statLog.debug('>>> '.join([s for s in output.decode('utf-8').strip().splitlines(True) if s.strip()]))
            except:
                statLog.debug('')
            if state_receive not in output.decode('utf-8'):
                False
            elif state_receive in output.decode('utf-8'):
                statLog.debug('### Return_until found: {} ###'.format(state_receive))
                return True, output_log
        return False, output_log

    def send_break(self, state_receive, sleep_timer=.1, timeout=5):
        self.ser.flushInput()
        self.ser.flushOutput()
        statLog.debug('### Sending echo. ###')
        start_time = time.time()
        timer = start_time + timeout
        output_log = ''
        # statLog.debug(''.join([s for s in output_log.strip().splitlines(True) if s.strip()]))
        time.sleep(sleep_timer)
        self.ser.write(b'echo')
        self.ser.write(b'\r\n')
        time.sleep(sleep_timer)
        self.ser.write(b'echo')
        self.ser.write(b'\r\n')
        time.sleep(sleep_timer)
        while start_time < timer:
            time.sleep(sleep_timer)
            start_time = time.time()
            output = self.ser.readline()
            output_log = output_log + output.decode('utf-8')
            statLog.debug('>>> '.join([s for s in output.decode('utf-8').strip().splitlines(True) if s.strip()]))
            if state_receive not in output.decode('utf-8'):
                False
            elif state_receive in output.decode('utf-8'):
                statLog.debug('### Send_break found: {} ###'.format(state_receive))
                return True, output_log
        return False, output_log

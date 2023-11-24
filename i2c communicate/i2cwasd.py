#!/usr/bin/python3
# -*- coding: utf-8 -*-

import smbus2 as sm
import termios
import sys
import tty

address_arduino1 = 0x50
address_arduino2 = 0x57

bus_i2c1 = sm.SMBus(1)
bus_i2c2 = sm.SMBus(0)

def read_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

speed_l = 0
speed_r = 0

while True:
    key = read_key()

    if key == 'W' or key == 'w':  # 'W' 키전진
        speed_l = 255
        speed_r = 255
    elif key == 'D' or key == 'd':  # 'D' 키 우선회
        speed_l = 50
        speed_r = 205
    elif key == 'A' or key == 'a':  # 'A' 키 좌선회
        speed_l = 205
        speed_r = 50
    elif key == 'S' or key == 's':  # 'S' 키 후진
        speed_l = 50
        speed_r = 50
    elif key == 'X' or key == 'x':  # 'X' 키 정지
        speed_l = 128
        speed_r = 128
    elif key == 'K' or key == 'k':  # 'K' 키 좌회전
        speed_l = 255
        speed_r = 80
    elif key == 'L' or key == 'l':  # 'L' 키 우회전
        speed_l = 80
        speed_r = 255

    bus_i2c1.write_byte(address_arduino1, speed_l)
    bus_i2c2.write_byte(address_arduino2, speed_r)

    number_arduino1 = bus_i2c1.read_byte(address_arduino1)
    number_arduino2 = bus_i2c2.read_byte(address_arduino2)

    print("from1:", number_arduino1)
    print("from2:", number_arduino2)

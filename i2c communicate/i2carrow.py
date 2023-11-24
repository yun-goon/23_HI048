#!/usr/bin/python3
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

    if key == '\x1b':  # Escape key (arrow keys send escape sequences)
        arrow_key = read_key()
        
        if arrow_key == '[':
            arrow_key = read_key()
            
            if arrow_key == 'A':  # Up Arrow
                speed_l = 100
                speed_r = 100
            elif arrow_key == 'C':  # Right Arrow
                speed_l = 0
                speed_r = 200
            elif arrow_key == 'D':  # Left Arrow
                speed_l = 200
                speed_r = 0
            elif arrow_key == 'B':  # Down Arrow
                speed_l =0
                speed_r =0

    bus_i2c1.write_byte(address_arduino1, speed_l)
    bus_i2c2.write_byte(address_arduino2, speed_r)

    number_arduino1 = bus_i2c1.read_byte(address_arduino1)
    number_arduino2 = bus_i2c2.read_byte(address_arduino2)

    print("from1:", number_arduino1)
    print("from2:", number_arduino2)

#!/usr/bin/python3
import smbus2 as sm

address_arduino1 = 0x50
address_arduino2 = 0x57


bus_i2c1 = sm.SMBus(1)

bus_i2c2 = sm.SMBus(0)

while True:
    speed_l = int(input("inputa"))
    speed_r = int(input("inputb"))

  
    bus_i2c1.write_byte(address_arduino1, speed_l)
    bus_i2c2.write_byte(address_arduino2, speed_r)

    number_arduino1 = bus_i2c1.read_byte(address_arduino1)
    number_arduino2 = bus_i2c2.read_byte(address_arduino2)

    print("from1:", number_arduino1)
    print("from2", number_arduino2)
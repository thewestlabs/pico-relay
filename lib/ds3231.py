#!/usr/bin/python
# -*- coding: utf-8 -*-
from machine import Pin, I2C
import time
import binascii

ALARM_PIN = 3

class ds3231(object):
    NowTime = b'\x00\x45\x13\x02\x24\x05\x21'
    w  = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
    address = 0x68
    start_reg = 0x00
    alarm1_reg = 0x07
    control_reg = 0x0e
    status_reg = 0x0f
    
    def __init__(self,i2c_port,i2c_scl,i2c_sda):
        self.bus = I2C(i2c_port,scl=Pin(i2c_scl),sda=Pin(i2c_sda))

    def set_time(self,new_time):
        hour = new_time[0] + new_time[1]
        minute = new_time[3] + new_time[4]
        second = new_time[6] + new_time[7]
        week = "0" + str(self.w.index(new_time.split(",",2)[1])+1)
        year = new_time.split(",",2)[2][2] + new_time.split(",",2)[2][3]
        month = new_time.split(",",2)[2][5] + new_time.split(",",2)[2][6]
        day = new_time.split(",",2)[2][8] + new_time.split(",",2)[2][9]
        now_time = binascii.unhexlify((second + " " + minute + " " + hour + " " + week + " " + day + " " + month + " " + year).replace(' ',''))
        #print(binascii.unhexlify((second + " " + minute + " " + hour + " " + week + " " + day + " " + month + " " + year).replace(' ','')))
        #print(self.NowTime)
        self.bus.writeto_mem(int(self.address),int(self.start_reg),now_time)
    
    def read_time(self):
        t = self.bus.readfrom_mem(int(self.address),int(self.start_reg),7)
        a = t[0]&0x7F  #second
        b = t[1]&0x7F  #minute
        c = t[2]&0x3F  #hour
        d = t[3]&0x07  #week
        e = t[4]&0x3F  #day
        f = t[5]&0x1F  #month
        return "20%x/%02x/%02x %02x:%02x:%02x %s" %(t[6],t[5],t[4],t[2],t[1],t[0],self.w[t[3]-1])


    def set_alarm_time(self,alarm_time):
        #    init the alarm pin
        self.alarm_pin = Pin(ALARM_PIN,Pin.IN,Pin.PULL_UP)
        #    set alarm irq
        self.alarm_pin.irq(lambda pin: print("alarm1 time is up"), Pin.IRQ_FALLING)
        #    enable the alarm1 reg
        self.bus.writeto_mem(int(self.address),int(self.control_reg),b'\x05')
        #    convert to the BCD format
        hour = alarm_time[0] + alarm_time[1]
        minute = alarm_time[3] + alarm_time[4]
        second = alarm_time[6] + alarm_time[7]
        date = alarm_time.split(",",2)[2][8] + alarm_time.split(",",2)[2][9]
        now_time = binascii.unhexlify((second + " " + minute + " " + hour +  " " + date).replace(' ',''))
        #    write alarm time to alarm1 reg
        self.bus.writeto_mem(int(self.address),int(self.alarm1_reg),now_time)

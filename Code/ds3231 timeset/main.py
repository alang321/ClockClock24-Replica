import urtc
import time
from machine import I2C, Pin

sda1=machine.Pin(14)
scl1=machine.Pin(3)
i2c=machine.I2C(1,sda=sda1, scl=scl1, freq=100000)

rtc = urtc.DS3231(i2c)
#datetime = urtc.datetime_tuple(year=2022, month=4, day=13, weekday=3, hour=12, minute=15, second=40, millisecond=0)
#rtc.datetime(datetime)

readtime = rtc.datetime()
print(readtime.year)
print(readtime.month)
print(readtime.day)
print(readtime.weekday)
print(readtime.hour)
print(readtime.minute)
print(readtime.second)
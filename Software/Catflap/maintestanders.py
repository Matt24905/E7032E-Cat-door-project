from machine import Pin, Timer, PWM
import time
import BatteryMonitor # Importing the BatteryMonitor function that we wrote.

button1 = Pin(15, Pin.IN, Pin.PULL_UP)  #Low button
BatteryCapacity = 2500 # Battery capacity in mAh, inargument
AverageCurrent = 1  # Average current consumption in mAh

BatteryVoltage, BatteryPercentage, BatteryPrecentageNEW, BatteryValue, BatteryLOW, BatteryDays = BatteryMonitor.BatteryMonitor(BatteryCapacity, AverageCurrent)
    
while True:
    if button1.value() == 1:

        print(BatteryVoltage)
        print(BatteryPercentage)
        print(BatteryPrecentageNEW)    
        print(BatteryValue)
        print(BatteryLOW)
        print(BatteryDays)    
        break
    
    
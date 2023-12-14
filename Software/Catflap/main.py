import time
from machine import Pin
from fakeData import *
from helpers import *
from connect import connectToWifi
from secrets import ssid, password
from buttons import *
import readtag.py
connectToWifi(ssid, password)

while True:
    #IR_sensor_reading = False
    if button3.value() == 0:
        print("You made it")
        #nuvarande kollar endast ifall en tag är där eller ej, returnerar true/false
        read_tag(pin_number=1, num_measurements=8000, delay_between_measurements_us=1,antenna_pin=0)
        pass
    elif button1.value() == 1 and button2.value() == 1:
        pass
    elif button1.value() == 0 and button2.value() == 1:
        addCat()
        blink(led1)
        pass
    elif button2.value() == 0 and button1.value() == 1:
        checkIfCat()
        blink(led3)
        pass
    else:
        print("Nothing is happening, I'm dying from boredom")

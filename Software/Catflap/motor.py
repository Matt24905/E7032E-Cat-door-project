import time
from machine import Pin

def turnOn(motor_a, motor_b):
    M_sleep = Pin(1, Pin.OUT) 
    M_sleep.value(1) # Activate the H-bridge driver from sleepmode
    motor_a.on()
    time.sleep(2)
    turnOff(motor_a)
    time.sleep(1)
    motor_b.on()
    time.sleep(2)
    turnOff(motor_b)
    
    
def turnOff(motor):
    motor.off()
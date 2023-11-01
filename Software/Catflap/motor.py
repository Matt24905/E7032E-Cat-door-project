from machine import Pin, Timer
import time

motor1 = Pin(5, Pin.OUT)
motor2 = Pin(6, Pin.OUT)
button2 = Pin(0, Pin.IN, Pin.PULL_UP)  #High button
button1 = Pin(15, Pin.IN, Pin.PULL_UP)  #Low button

M_sleep = Pin(1, Pin.OUT) 
M_sleep.value(1) # Activate the H-bridge driver from sleepmode

ledR = Pin(4, Pin.OUT)
#ledR.value(0)

ledG = Pin(3, Pin.OUT)
#ledG.value(0)

ledB = Pin(2, Pin.OUT)
#ledB.value(0)

def turnOn(motor_a, motor_b):
    motor_a.on()
    ledB.value(1)
    time.sleep(0.07)
    ledB.value(0)
    turnOff(motor_a)
    time.sleep(1)
    motor_b.on()
    time.sleep(0.07)
    turnOff(motor_b)
    
    
def turnOff(motor):
    motor.off()
    
#Using buttons for now, will get input from antenna later
while True:
    if button1.value() == 1 and button2.value() == 1:
        pass
    elif button1.value() == 0 and button2.value() == 1:
        turnOn(motor1, motor2)
    elif button2.value() == 0 and button1.value() == 1:
        turnOn(motor2, motor1)
    else:
        print("Don't wanna")
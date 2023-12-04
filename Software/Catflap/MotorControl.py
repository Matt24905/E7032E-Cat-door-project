from machine import Pin, Timer
import time

motor1 = Pin(5, Pin.OUT)
motor2 = Pin(6, Pin.OUT)
Motor_Sleep = Pin(1, Pin.OUT) # Motor Sleep pin 

def Unlock():
    Motor_Sleep.on()	# Turn on the H-Bridge IC.	Has a wake time of 30us.
    motor1.on()			# Enable one pin of the Motor control to make it spin in one direction.
    time.sleep(0.07)	# Delay 70ms in order to make sure the motor have the time to Unlock/Lock.
    turnOff(motor1)		# Turn off one pin of the motorControl to make it stop.
    Motor_Sleep.off()	# Turn off the H-Bridge IC.
    
def Lock():
    Motor_Sleep.on()
    motor2.on()
    time.sleep(0.07)
    turnOff(motor2)
    Motor_Sleep.off()
    
def Unlock_Lock(LockDelay):
    Motor_Sleep.on()
    motor1.on()
    time.sleep(0.07)
    turnOff(motor1)
    time.sleep(LockDelay)	# Uncertain about sleep in the entire system. Make better when know what to do.
    motor2.on()
    time.sleep(0.07)
    turnOff(motor2)
    Motor_Sleep.off()    
    
def turnOff(motor):
    motor.off()

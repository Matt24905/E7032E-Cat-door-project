from machine import Pin, Timer, PWM
import time
from helpers import led1, led2, led3

led1.freq(5000)
led2.freq(5000)
led3.freq(5000)

def blink(led):
    for i in range(5):
        led.duty_u16(5000)
        time.sleep(0.5)
        led.duty_u16(0)
        time.sleep(0.5)
 
#Time sleep defines how long the LED is on
def static(led):
    led.duty_u16(5000)
    time.sleep(1)
    led.duty_u16(0)

def pickButton(button, led):
    while button.value()== 1:
        pass
    t=time.ticks_ms()
    time.sleep_ms(1)
    while button.value()== 0:
        pass
    t=time.ticks_diff(time.ticks_ms(),t)
    if t<1500:
        blink(led)
        addCat()
    else:
        static(led)
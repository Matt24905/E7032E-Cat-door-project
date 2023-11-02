from machine import Pin, Timer, PWM
import time

led1 = PWM(Pin(4, Pin.OUT)) 				  #Red
led2 = PWM(Pin(3, Pin.OUT))					  #Green
led3 = PWM(Pin(2, Pin.OUT)) 				  #Blue
button2 = Pin(0, Pin.IN, Pin.PULL_UP)  #High button
button1 = Pin(15, Pin.IN, Pin.PULL_UP)  #Low button
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

def pickButton(button, led_a, led_b):
    while button.value()== 1:
        pass
    t=time.ticks_ms()
    time.sleep_ms(1)
    while button.value()== 0:
        pass
    t=time.ticks_diff(time.ticks_ms(),t)
    if t<1500:
        blink(led_a)
    else:
        static(led_b)

while True:
    if button1.value() == 1 and button2.value() == 1:
        pass
    elif button1.value() == 0 and button2.value() == 1:
        pickButton(button1, led2, led1)
    elif button2.value() == 0 and button1.value() == 1:
        pickButton(button2, led3, led1)
    else:
        print("Don't wanna")

from machine import Pin, PWM
import time

# led = Pin('LED', Pin.OUT)
# button1 = Pin(18, Pin.IN, Pin.PULL_DOWN)  #High button
# button2 = Pin(27, Pin.IN, Pin.PULL_DOWN)  #High button
# motor1 = Pin(21, Pin.OUT) 			#Red
# motor2 = Pin(20, Pin.OUT)			#Green
# led3 = Pin(19, Pin.OUT) 			#Blue
# button3 = Pin(17, Pin.IN, Pin.PULL_DOWN) 

##USE THESE FOR THE ACTUAL CATFLAP
button1 = Pin(0, Pin.IN, Pin.PULL_UP)  #Add cat button
button2 = Pin(15, Pin.IN, Pin.PULL_UP) #Settings button
led1 = PWM(Pin(4, Pin.OUT)) 				  #Red
led2 = PWM(Pin(3, Pin.OUT))					  #Green
led3 = PWM(Pin(2, Pin.OUT)) 				  #Blue
motor1 = Pin(5, Pin.OUT)
motor2 = Pin(6, Pin.OUT)
button3 = Pin(18, Pin.IN, Pin.PULL_UP)
led = Pin('LED', Pin.OUT)


def getTime():
    current_time = time.localtime()
    temp = [int(d) for  d in str(current_time[4])]
    if len(temp) == 1:
        temp.insert(0, 0)
    temp2 = ''.join(str(e) for e in temp)
    timestamp = str(current_time[3])+":"+temp2
    date = str(current_time[2])+"/"+str(current_time[1])+" "+str(current_time[0])
    return timestamp, date

def getUserInput():
    wifi = input("Enter wifi name: ")
    password = input("Enter password: ")
    return wifi, password

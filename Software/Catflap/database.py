import machine
import urequests as requests
import network
import time
from machine import Pin


# Add wifi name and password here, along with mongodb URL and API-key
SSID = "Matildas iPhone"
PSK = "12345678"
URL = "https://eu-central-1.aws.data.mongodb-api.com/app/data-xlqqs/endpoint/data/v1"
API_KEY =  "ahBPumzhigb9Ekt27BsGqomakzpPP3fEssHEDGWrvxl6ou9zWeKspX5v5ZmYge2t"

def connect_to_wifi(ssid, psk):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, psk)
    while not wlan.isconnected() and wlan.status() >= 0:
        print("Connecting...")
        time.sleep(5)
    if not wlan.isconnected():
        raise Exception("Wifi not available")
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return wlan

def disconnect_wifi(wlan):
    try:
        wlan.active(False)
    except Exception as e:
        print(e)
        
def findOne(filter_dictionary):
    try:
        headers = {"api-key": API_KEY}
        searchPayload = {
            "dataSource": "Pico",
            "database": "Catflap",
            "collection": "Cats",
            "filter": filter_dictionary,
        }
        response = requests.post(URL + "/action/findOne", headers=headers, json=searchPayload)
        print("Response: (" + str(response.status_code) + "), msg = " + str(response.text))
        if response.status_code >= 200 and response.status_code < 300:
            print("Success Response")
        else:
            print(response.status_code)
            print("Error")
        response.close()
    except Exception as e:
        print(e)


def insertOne(filter_dictionary):
    try:
        headers = {"api-key": API_KEY}
        insertPayload = {
            "dataSource": "Pico",
            "database": "Catflap",
            "collection": "Cats",
            "document": filter_dictionary,
        }
        response = requests.post(URL + "/action/insertOne", headers=headers, json=insertPayload)
        print(response)
        print("Response: (" + str(response.status_code) + "), msg = " + str(response.text))
        if response.status_code >= 200 and response.status_code < 300:
            print("Success Response")
        else:
            print(response.status_code)
            print("Error")
        response.close()
    except Exception as e:
        print(e)

def deleteOne(filter_dictionary):
    try:
        headers = {"api-key": API_KEY}
        searchPayload = {
            "dataSource": "Pico",
            "database": "Catflap",
            "collection": "Cats",
            "filter": filter_dictionary,
        }
        response = requests.post(URL + "/action/deleteOne", headers=headers, json=searchPayload)
        print("Response: (" + str(response.status_code) + "), msg = " + str(response.text))
        if response.status_code >= 200 and response.status_code < 300:
            print("Success Response")
        else:
            print(response.status_code)
            print("Error")
        response.close()
    except Exception as e:
        print(e)

led = Pin('LED', Pin.OUT) 				  #Red
button1 = Pin(21, Pin.IN, Pin.PULL_DOWN)  #High button
button2 = Pin(26, Pin.IN, Pin.PULL_DOWN)  #High button

connect_to_wifi(SSID, PSK)

def blink(led):
    for i in range(5):
        led.toggle()
        time.sleep(0.5)
        led.off()
 
#Time sleep defines how long the LED is on
def static(led):
    led.on()
    time.sleep(3)
    led.off()

def pickButton(button):
    while button.value()== 0:
        pass
    t=time.ticks_ms()
    time.sleep_ms(1)
    while button.value()== 1:
        pass
    t=time.ticks_diff(time.ticks_ms(),t)
    if t<1500:
        blink(led)
    else:
        static(led)

while True:
    if button1.value() == 0 and button2.value() == 0:
        pass
    elif button1.value() == 1 and button2.value() == 0:
        pickButton(button1)
        insertOne({"device": "MyPico", "readings": ["Button pressed"]})
    elif button2.value() == 1 and button1.value() == 0:
        pickButton(button2)
        deleteOne({"device": "MyPico", "readings": ["Button pressed"]})
    else:
        print("Don't wanna")


#findOne({"device": "MyPico", "readings": [3, "hello"]})
#deleteOne({"device": "MyPico", "readings": [1]})
#insertOne({"device": "MyPico", "readings": [3, "hello"]})


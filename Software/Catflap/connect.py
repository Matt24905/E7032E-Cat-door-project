import network
import time
from helpers import getUserInput
from secrets import ssid, password

def connectToWifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected() and wlan.status() >= 0:
        print("Connecting...")
        time.sleep(5)
    if not wlan.isconnected():
        raise Exception("Wifi not available")
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return wlan

def disconnectWifi(wlan):
    try:
        wlan.active(False)
        print("Disconnected")
    except Exception as e:
        print(e)
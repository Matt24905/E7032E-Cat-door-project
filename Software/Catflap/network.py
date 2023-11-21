import machine
from machine import Pin
import socket
import urequests as requests
from picozero import pico_temp_sensor
import network
import time

SSID = "Matildas iPhone"
PSK = "12345678"
led = Pin(5, Pin.OUT) 				  #Red


def connect_to_wifi(ssid, psk):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, psk)

    while not wlan.isconnected() and wlan.status() >= 0:
        print("Waiting to Connect")
        time.sleep(1)
    if not wlan.isconnected():
        raise Exception("Wifi not available")
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

def webpage(temperature, state):
    html = f"""
        <!DOCTYPE html>
        <html>
        <form action="./lighton">
        <input type="submit" value="Light on" />
        </form>
        <form action="./lightoff">
        <input type="submit" value="Light off" />
        </form>
        <p>LED is {state}</p>
        <p>Temperature is {temperature}</p>
        </body>
        </html>
        """
    return str(html)


def open_socket(ip):
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

def serve(connection):
    #Start a web server
    state = 'OFF'
    led.off()
    temperature = 0
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        try:
            request = request.split()[1]
        except IndexError:
            pass
        if request == '/lighton?':
            led.on()
            state = 'ON'
        elif request =='/lightoff?':
            led.off()
            state = 'OFF'
        temperature = pico_temp_sensor.temp
        html = webpage(temperature, state)
        client.send(html)
        client.close()

try:
    ip = connect_to_wifi(SSID, PSK)
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()
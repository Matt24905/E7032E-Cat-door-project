from machine import Pin
import utime

button1 = Pin(0, Pin.IN, Pin.PULL_UP)

readings = []

# Function to measure values and append them to the readings list
def measure(pin):
    value = pin.value()
    readings.append(value)

# Set up the approximate interval in microseconds (0.05ms = 50 microseconds)
interval_micros = 50

# Measure values at the specified interval until 8000 readings are obtained
while len(readings) < 8000:
    start_time = utime.ticks_us()  # Get the current time in microseconds
    measure(button1)
    # Wait to approximate the desired interval
    while utime.ticks_diff(utime.ticks_us(), start_time) < interval_micros:
        pass

# Save readings to a file
with open('readings.txt', 'w') as file:
    for reading in readings:
        file.write(str(reading) + '\n')

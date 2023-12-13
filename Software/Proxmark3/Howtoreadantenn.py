import machine
import utime

# Define the GPIO pin you want to measure
gpio_pin = machine.Pin(0, machine.Pin.IN)  # Change 14 to the GPIO pin you're using

# Create a list to store measured values
measurements = []

# Perform 32 measurements within 500us timeframe
start_time = utime.ticks_us()

for _ in range(8000):
    # Read the GPIO pin value and store it
    pin_value = gpio_pin.value()
    measurements.append(pin_value)
    utime.sleep_us(1)  # Adjust this delay as needed based on measurement requirements

end_time = utime.ticks_us()

# Calculate the actual time taken
elapsed_time = utime.ticks_diff(end_time, start_time)

# Save the measurements to a file
em = 'em.txt'
with open(em, 'w') as file:
    for value in measurements:
        file.write(str(value) + '\n')

print("Measurement complete. Data saved to", em)

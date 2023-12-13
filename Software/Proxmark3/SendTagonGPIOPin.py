from machine import Pin
import utime
while True:
    # Define the pin you want to use
    output_pin = Pin(0, Pin.OUT)

    # Define your bit string
  #  bit_string = "1111111110000011101000000000000000101000100111011111010010100010"
    #bit_string = "10101010101010101001010101010101010101010100101010101010101010101010101001010101010"
    bit_string = "10101010101010101001010101011010100110010101010101010101010101010101100110010101100101101010011010101010011001011001100101011001"
    # Set the approximate delay time between bits (in microseconds)
    delay_micros = 200
  #  delay_micros = 50

    # Loop through each bit in the string
    for bit in bit_string:
        # Set the pin according to the bit value
        output_pin.value(int(bit))

        # Wait for the specified delay
        utime.sleep_us(int(delay_micros))

    # Make sure to turn off the pin at the end
    output_pin.value(0)


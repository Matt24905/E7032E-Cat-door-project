
import utime
from machine import Pin, PWM

def measure_pin_with_delay(pin_number, num_measurements, delay_us):
    gpio_pin = Pin(pin_number, Pin.IN)  # Initialize the specified pin as an input

    measurements = []  # Create a list to store measured values

    for _ in range(num_measurements):
        pin_value = gpio_pin.value()  # Read the GPIO pin value and store it
        measurements.append(pin_value)
        utime.sleep_us(delay_us)  # Introduce a delay between measurements

    return measurements




def generate_125kHz_pwm(pin_number):
    # Configure the pin as an output
    pin = Pin(pin_number)
    pin.init(Pin.OUT)

    # Initialize PWM on the specified pin with a frequency of 125 kHz and a 50% duty cycle
    pwm = PWM(pin)
    pwm.freq(125000)  # Set PWM frequency to 125 kHz
    pwm.duty_u16(32768)  # Set 50% duty cycle (50% of 2^16 = 32768)
    return pwm

def find_transition_indices(data):
    transition_indices = []
    for i in range(1, len(data)):
        if data[i] != data[i - 1]:
            transition_indices.append(i)
    return transition_indices

def find_1_to_0_transitions(data):
    transitions_1_to_0 = []
    for i in range(1, len(data)):
        if data[i - 1] == 1 and data[i] == 0:
            transitions_1_to_0.append(i)
    return transitions_1_to_0


def calculate_median(lst):
    n = len(lst)
    s = sorted(lst)
    return (s[n//2-1]/2.0+s[n//2]/2.0, s[n//2])[n % 2] if n else None
def process_data(data_list, transition_indices, transitions_1_to_0):
    approx_step = round(calculate_median([transition_indices[i] - transition_indices[i - 1] for i in range(1, len(transition_indices))]) * 1.15)

    transistion_counter = 0
    delbit = []
    delbitkoord = []
    i = 0
    while i < len(data_list):
        segment_start = i
        if segment_start >= transition_indices[transistion_counter]:
            segment_start = transition_indices[transistion_counter]
            transistion_counter += 1

        segment_end = segment_start + approx_step

        if segment_end > len(data_list):
            break

        segment_data = sum(data_list[segment_start:segment_end])
        segment_data /= approx_step

        i = segment_end
        delbitkoord.append(segment_start)

        if segment_data > 0.4:
            delbit.append(1)
        else:
            delbit.append(0)

    return delbit, delbitkoord, transition_indices


def find_start_of_pattern(signal, pattern):
    signal_str = ''.join(map(str, signal))  # Convert the signal list to a string
    pattern_str = ''.join(map(str, pattern))  # Convert the pattern list to a string
    
    start_index = signal_str.find(pattern_str)
    
    if start_index != -1:
        return start_index + len(pattern_str)
    else:
        return -1  # Return -1 if the pattern is not found
def flip_bits_list(bit_list):
    flipped_list = [1 if bit == 0 else 0 for bit in bit_list]
    return flipped_list

def decode_manchester_signal(signal):
    #signal = flip_bits_list(signal)
    pattern = [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]  # Define the pattern to search for
    start_index = find_start_of_pattern(signal, pattern)
    #print(start_index)
    start_index = start_index - 18
    
    if start_index != -1:
        #print('start found')
        encoded_signal = signal[start_index:len(signal)]
        
    decoded_binary = []  # Initialize an empty list to store the decoded binary sequence

    for i in range(0, len(encoded_signal), 2):  # Processing pairs of values (each pair represents one bit)
        current_bit = encoded_signal[i:i + 2]  # Extracting the current pair (each pair represents one bit in Manchester)

        if current_bit == [0, 1]:  # Decoding '01' to '0' in binary
            decoded_binary.append('0')
        elif current_bit == [1, 0]:  # Decoding '10' to '1' in binary
            decoded_binary.append('1')
        #else:
            
            #decoded_binary.append('2')
            #return "Invalid Manchester encoding sequence", ''  # Return an error for invalid sequence

    return ''.join(decoded_binary)  # Return the decoded binary sequence as a string
        

def EM410Protocol(output_array):
    # Convert output_array to a string
    #output_string = ''.join(map(str, output_array))
    output_string = output_array
    # Define the header pattern
    header_pattern = "111111111"

    # Find the starting position of the header pattern
    start_index = output_string.find(header_pattern)

    if start_index != -1:
        # Move past the header pattern
        start_index += len(header_pattern)

        hex_values = []  # Initialize an empty list to store hex values

        # Check 5-bit sequences and their even parity 10 times
        for _ in range(10):
            current_sequence = output_string[start_index:start_index + 5]

            if len(current_sequence) == 5:
                ones_count = current_sequence.count('1')
                is_even_parity = ones_count % 2 == 0

                # Decode the first 4 bits to hexadecimal and append to the hex_values list
                hex_val = hex(int(current_sequence[:4], 2))[2:].upper()
                hex_values.append(hex_val)

            else:
                return "Incomplete sequence of 5 bits", ''.join(hex_values)  # Return incomplete sequence error

            start_index += 5  # Move to the next 5-bit sequence

        hex_string = ''.join(hex_values)  # Concatenate the hex values into a single string

        if output_string[start_index + 4] == '0':
            hex_string = ''.join(hex_values)
            return None, hex_string
        else:
            return "Stop bit mismatch", ''.join(hex_values)

    else:
        return "Header pattern not found", ''
    
def turn_off_antenna(pwm_object, pin_number):
    #print('Turning off antenna')
    # Stop the PWM signal
    pwm_object.deinit()
    
    # Deinitialize the pin used for PWM
    pin = Pin(pin_number)
    pin.init(Pin.IN)
#kalla på funktioner    
####

# Function to perform tag reading and handle errors
def read_tag(pin_number, num_measurements, delay_between_measurements_us,antenna_pin):
    generate_125kHz_pwm(antenna_pin)
    pwm = generate_125kHz_pwm(antenna_pin)    
    try:
        result = measure_pin_with_delay(pin_number, num_measurements, delay_between_measurements_us)
        #print("Measured values:", result)

        data_list = result
        transition_indices = find_transition_indices(data_list)
        transitions_1_to_0 = find_1_to_0_transitions(data_list)

        delbit, delbitkoord, transition_indices = process_data(data_list, transition_indices, transitions_1_to_0)

        print("Delbit:", delbit)
        #print("Delbitkoord:", delbitkoord)
        #print("Transition indices:", transition_indices)

        mes = decode_manchester_signal(delbit)
        print("binart:", mes)
        avkok = EM410Protocol(mes)
        turn_off_antenna(pwm, pin_number)

        if avkok is not None:
            print(avkok)
            return True
        else:
            print("Tag read successfully:", avkok)
            turn_off_antenna(pwm, pin_number)
            return True

    except Exception as e:
        #print("Error occurred while processing signal:", e)
        turn_off_antenna(pwm, pin_number)
        return False

        # Handle error cases or perform necessary actions here

pin_number = 1
antenna_pin = 0
num_measurements = 8000
delay_between_measurements_us = 1

status = read_tag(pin_number=1, num_measurements=8000, delay_between_measurements_us=1,antenna_pin=0)
print(status)

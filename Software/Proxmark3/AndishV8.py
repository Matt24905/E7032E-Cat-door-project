from machine import Pin, ADC
import utime


#def rapid_read_gpio_values(pin_number, duration_us):
    
    #gpio_pin = machine.Pin(pin_number, machine.Pin.IN, machine.Pin.PULL_DOWN)
    #end_time = utime.ticks_add(utime.ticks_us(), duration_us)
   # measurements = []

  #  while utime.ticks_diff(end_time, utime.ticks_us()) > 0:
 #       measurements.append(gpio_pin.value())
    
#    with open("EMBINARY.txt", "r") as file:
    #with open("GoodTestEM410x.pm3", "r") as file:
 #       measurements = [int(value) for value in file.read().split()]

#    return measurements

def rapid_read_gpio_values(pin_number, duration_us):
    adc = ADC(Pin(26))
    end_time = utime.ticks_add(utime.ticks_us(), duration_us)
    measurements = []
    while utime.ticks_diff(end_time, utime.ticks_us()) > 0:
        measurements.append(adc.read_u16()) # Reads a 16-bit value
    #print(measurements)  
    digital_values = []
    for value in measurements:
        digital_values.append(1 if value >= 2**15 else 0)            
    measurements = digital_values
    return measurements



# classify_and_convert
def classify_and_convert(data, min_threshold, max_threshold):
    bits = []
    current_value = data[0]
    count = 0
    avg_count = []

    for value in data:
        if value == current_value:
            count += 1
        else:
            # Calculate the average pulse length if we have enough data
            if avg_count:
                avg_pulse_length = sum(avg_count) / len(avg_count)
                threshold = (min_threshold + avg_pulse_length) / 2
                #print('ang',threshold)

            # Use max_threshold if we don't have enough pulse length data
            else:
                threshold = max_threshold

            # Classify based on the adaptive threshold
            if count >= threshold:
                bits.extend([current_value, current_value])
                avg_count.append(count)  # Add to the average pulse length data
            else:
                bits.append(current_value)

            count = 1
            current_value = value

    # Handle the last segment using the most recent threshold
    if count >= threshold:
        bits.extend([current_value, current_value])
    else:
        bits.append(current_value)
        

    return bits






# process_gpio_signal
def process_gpio_signal(values):
    # Check if the input array is empty
    if not values:
        return "Input array is empty"
    
    # Find the index where the header pattern starts
    header_pattern = [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]  # Converted to a list of integers
    i = -1  # Initialize i to -1
    for j in range(len(values) - 18):
        if values[j:j + 19] == header_pattern:
            i = j  # Assign the found index to i
            break
    if i == -1:
        return "Header pattern not found"

    # Calculate the end index based on the start index and total bits to capture
    if i + 129 > len(values):
        return "Header pattern found, but data is too short"

    # Extract the relevant portion of the signal after the header pattern
    captured_bits = values[i + 1:i + 129]

    return captured_bits

# decode_inverted_manchester
def decode_inverted_manchester(encoded_signal):
    decoded_bits = []

    # Loop through the signal, two elements at a time
    for i in range(0, 127, 2):
        # Combine the two bits for easier comparison
        bit_pair = (encoded_signal[i], encoded_signal[i+1])

        # Check for transitions and decode
        if bit_pair == (1, 0):
            decoded_bits.append(1)
        elif bit_pair == (0, 1):
            decoded_bits.append(0)
        # Optional: Handle invalid transitions, e.g., (0, 0) or (1, 1)
        else:
            # Handle invalid transition
            break
    # Convert the list of bits into a string
    decoded_string = ''.join(str(bit) for bit in decoded_bits)
    return decoded_bits

def decode_em4100(bit_list):
    if len(bit_list) != 64:
        return "Invalid input: List not correct length."

    if bit_list[:9] != [1, 1, 1, 1, 1, 1, 1, 1, 1]:
        return "Invalid input: Header bits are incorrect."

    if bit_list[-1] != 0:
        return "Invalid input: Stop bit is incorrect."

    data_bits_with_parity = bit_list[9:-5]
    data_bits = []

    for i in range(0, len(data_bits_with_parity), 5):
        data = data_bits_with_parity[i:i+4]
        parity = data_bits_with_parity[i+4]
        if sum(data) % 2 != parity:
            return f"Invalid input: Parity check failed for group {data}"
        data_bits.extend(data)

    bit_string = ''.join(map(str, data_bits))
    hex_result = '{:0>10}'.format(hex(int(bit_string, 2))[2:].upper())
    return hex_result



# Example usage
def main():
    while True:

        # Measure ra256pidly for 65536 microseconds

        raw_measurements = rapid_read_gpio_values(0, 65536)
        #print("rapid_read_analog_values",raw_measurements)
        threshold = 12 # Example threshold, adjust based on your data
        thresholdMAX = 25
        converted_bits = classify_and_convert(raw_measurements, threshold,thresholdMAX)
        #print("classify_and_convert",converted_bits)
        captured_bits = process_gpio_signal(converted_bits)
        #print("process_gpio_signal",converted_bits)
        # Check if captured_bits is a string message or actual data
        if isinstance(captured_bits, str):
            #print(captured_bits)  # Print error message
            # Delay before the next read if the header pattern is not found or data is too short
            #utime.sleep(1)
            continue  # Skip the rest of the loop and try again

        decoded_signal = decode_inverted_manchester(captured_bits)
        #decoded_signal = '1111111110000011101000000000000000101000100111011111010010100010'
        #print('MAN',decoded_signal)
            # Should be 0E000A4DE2
        valid_tag = decode_em4100(decoded_signal)
        if "Invalid input" not in valid_tag:
            print("Valid tag found:", valid_tag)
            #break  # Exit the loop if a valid tag is found
            #else:
                #print(valid_tag)  # Print the error message
                #utime.sleep(1)  # Delay before the next read if the tag is invalid
    # Run the main function
main()






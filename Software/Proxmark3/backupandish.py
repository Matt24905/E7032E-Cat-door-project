import machine
import utime


# read_gpio_values
def read_gpio_values(pin_number, num_measurements=256, delay_us=236): # Should be 256 but maybe raspberryn need some time to measure again.
    gpio_pin = machine.Pin(pin_number, machine.Pin.IN, machine.Pin.PULL_DOWN)
    measurements = []
    for _ in range(num_measurements):
        measurements.append(gpio_pin.value())
        utime.sleep_us(delay_us)
        
    return measurements

# process_gpio_signal
def process_gpio_signal(values, header_pattern, total_bits=110):
    # Find the index where the header pattern starts
    start_index = ''.join(map(str, values)).find(header_pattern)
    if start_index == -1:
        return "Header pattern not found"

    # Calculate the end index based on the start index and total bits to capture
    end_index = start_index + len(header_pattern) + total_bits
    if end_index > len(values):
        return "Header pattern found, but data is too short"

    # Extract the relevant portion of the signal after the header pattern
    captured_bits = values[start_index + 1:end_index]
    
    return captured_bits

# decode_inverted_manchester
def decode_inverted_manchester(encoded_signal):
    decoded_bits = []
    # Loop through the signal, two elements at a time
    for i in range(0, len(encoded_signal), 2):
        # Get the pair of signal states representing one bit
        first_bit = encoded_signal[i]
        second_bit = encoded_signal[i+1] if i+1 < len(encoded_signal) else None
        
        # Check for the transitions specific to inverted Manchester encoding
        if first_bit is not None and second_bit is not None:
            # A high-to-low transition represents a logical '1'
            if first_bit == 1 and second_bit == 0:
                decoded_bits.append(1)
            # A low-to-high transition represents a logical '0'
            elif first_bit == 0 and second_bit == 1:
                decoded_bits.append(0)
            # If the pair is not a valid Manchester code, you might want to handle the error
            else:
                # Handle invalid transition (e.g., 00 or 11)
                # You could raise an error, append a special value, or continue
                pass
    
    # Remove when testing Convert the list of bits into a string
    decoded_string = ''.join(str(bit) for bit in decoded_bits)
    return decoded_string

# decode_em4100
def decode_em4100(array):
    # Assuming the array starts with a 9-bit header followed by 10 groups of 4 data bits and a parity bit.
    # It ends with 4 column parity bits and a stop bit.
    if len(array) != 64:
       return "Invalid input: String not correct length."

    # Check if the input array starts with 9 header bits all set to '1'
    if array[:9] != '111111111':
        return "Invalid input: Header bits are incorrect."
    
    # Check if the stop bit is '0'
    if array[-1] != '0':
        return "Invalid input: Stop bit is incorrect."
    
    # Split the input array into data bits and parity bits
    data_bits_with_parity = array[9:-5]  # Exclude header, column parity and stop bits
    groups = [data_bits_with_parity[i:i+5] for i in range(0, len(data_bits_with_parity), 5)]  # Split into groups of 4 data bits + 1 parity bit
    
    # Check and collect the data bits
    data_bits = ''
    for group in groups:
        data = group[:4]  # First 4 bits are data
        parity = group[4]  # 5th bit is parity
        if data.count('1') % 2 != int(parity):  # Even parity check
            return "Invalid input: Parity check failed for group " + data
        data_bits += data  # Collect data bits
    
    # Convert data bits to hexadecimal and ensure it is padded to maintain a fixed length with leading zeroes if necessary
    hex_result = '{:0>10}'.format(hex(int(data_bits, 2))[2:].upper())
    
    return hex_result


# Example usage
def main():
    gpio_pin_number = 0  # GPIO pin number
    header_pattern = '1101010101010101010'  # Your specific header pattern

    while True:
        gpio_values = read_gpio_values(gpio_pin_number)  # Read the GPIO values
        
        #gpio_values = '1010101010101100110010101100101101010011010101010011001011001100101011001101010101010101010010101010110101001100101010101010101010101010101011001100101011001011010100110101010100110010110011001010110011010101010101010100101010101101010011001010101010101010'
        #gpio_values = [int(gpio_values) for gpio_values in gpio_values]
        #print("Measurement", gpio_values)
        captured_bits = process_gpio_signal(gpio_values, header_pattern)
        print("Process_gpio_signal", captured_bits)

        # Check if captured_bits is a string message or actual data
        if isinstance(captured_bits, str):
            print(captured_bits)  # Print error message
            # Delay before the next read if the header pattern is not found or data is too short
            #utime.sleep(1)
            continue  # Skip the rest of the loop and try again


        # Remove when test
        #captured_bits = '10101010101010101001010101011010100110010101010101010101010101010101100110010101100101101010011010101010011001011001100101011001'
        #captured_bits = [int(captured_bits) for captured_bits in captured_bits]
        
        decoded_signal = decode_inverted_manchester(captured_bits)
        print("Decode_inverted_manchester:", decoded_signal)
        #decoded_signal = '1111111110000011101000000000000000101000100111011111010010100010'
        # Should be 0E000A4DE2
        valid_tag = decode_em4100(decoded_signal)
        if "Invalid input" not in valid_tag:
            print("Valid tag found:", valid_tag)
            break  # Exit the loop if a valid tag is found
        else:
            print(valid_tag)  # Print the error message
            #utime.sleep(1)  # Delay before the next read if the tag is invalid

# Run the main function
main()





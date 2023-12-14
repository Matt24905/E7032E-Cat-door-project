import machine
import utime


# Signal processing functions (calculate_median, find_crossings, etc.) go here

def read_gpio_values(pin_number, num_measurements=5000, delay_us=1):
    gpio_pin = machine.Pin(pin_number, machine.Pin.IN, machine.Pin.PULL_DOWN)
    measurements = []
    for _ in range(num_measurements):
        measurements.append(gpio_pin.value())
        utime.sleep_us(delay_us)
    return measurements

def process_gpio_signal(values, header_pattern, total_bits=64):
    crossings = find_crossings(values)
    diff_lengths = [crossings[i] - crossings[i - 1] for i in range(1, len(crossings))]
    approx_step = round(calculate_median(diff_lengths))

    new_array = create_new_array(crossings, approx_step)
    output_array = ''.join([str(measure_left_right(values, crossing, approx_step)) for crossing in new_array])

    start_index = output_array.find(header_pattern)
    if start_index == -1:
        return "Header pattern not found"

    end_index = start_index + total_bits
    return output_array[start_index:end_index] if end_index <= len(output_array) else "Header pattern found, but data is too short"


def find_crossings(values):
    """Find the indices where the value changes from non-positive to positive."""
    return [i for i in range(1, len(values)) if values[i - 1] <= 0 and values[i] > 0]

def calculate_median(lst):
    """Calculate the median of a list."""
    n = len(lst)
    if n == 0:
        return None
    lst = sorted(lst)
    mid = n // 2
    return (lst[mid - 1] + lst[mid]) / 2 if n % 2 == 0 else lst[mid]

def create_new_array(crossings, approx_step):
    """Create a new array using the crossing points and the approximate step."""
    if not crossings:
        return []
    
    # Correct Anders-tag: 0E000A4DE2
    # Choose a middle crossing as the starting point
    middle_index = len(crossings) // 128
    #start_value = crossings[10]
    start_value = crossings[middle_index]

    # Calculate the last value based on the chosen start value
    last_value = crossings[-1] + approx_step

    # Create a new array starting from the middle crossing
    return list(range(start_value, last_value, approx_step))


def measure_left_right(values, index, approx_step):
    """Measure and compare the sum of values to the left and right of a given index."""
    left_index = max(0, index - approx_step // 2)
    right_index = min(len(values), index + approx_step // 2)
    return 1 if sum(values[left_index:index]) > sum(values[index:right_index]) else 0



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


def main():
    gpio_pin_number = 0  # GPIO pin number
    header_pattern = '111111111'  # Header pattern to look for

    while True:
        # Read values from GPIO pin
        gpio_values = read_gpio_values(gpio_pin_number)

        # Process the signal from GPIO pin values
        binary_output = process_gpio_signal(gpio_values, header_pattern)
        #print(binary_output)
        # If a valid header pattern is not found, continue reading
        if binary_output == "Header pattern not found":
            #print("Header pattern not found, continuing...")
            #utime.sleep(1)  # Add a delay to avoid high CPU usage
            continue
        #binary_output = '1111111110000011101000000000000000101000100111011111010010100010'
        # Decode the EM4100 protocol from the binary output
        decode_result = decode_em4100(binary_output)

        # Check if the decoded result is valid
        if "Invalid input" not in decode_result:
            print("Valid tag found:", decode_result)
            #break
        #else:
            #print(decode_result)
           # utime.sleep(1)  # Add a delay before trying again

# Run the main function
main()
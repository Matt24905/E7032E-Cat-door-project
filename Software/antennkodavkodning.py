def read_file(filename):
    with open(filename, "r") as file:
        data_list = []
        for line in file:
            elements = line.strip().split(',')  # Change delimiter if needed
            converted_elements = [int(elem) for elem in elements]
            data_list.append(converted_elements)
        return data_list

def find_transition_indices(data):
    transition_indices = []
    for i in range(1, len(data)):
        if data[i] != data[i - 1]:
            transition_indices.append(i)
    return transition_indices

def find_1_to_0_transitions(data):
    transitions_1_to_0 = []
    for i in range(1, len(data)):
        if data[i - 1][0] == 1 and data[i][0] == 0:
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
    flat_data_list = [item for sublist in data_list for item in sublist]
    
    while i < len(flat_data_list):
        segment_start = i
        if segment_start >= transition_indices[transistion_counter]:
            segment_start = transition_indices[transistion_counter]
            transistion_counter += 1
        
        segment_end = segment_start + approx_step
        segment_data = sum(flat_data_list[segment_start:segment_end])
        segment_data /= approx_step
        
        if segment_end > len(flat_data_list):
            break
        
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

def decode_manchester_signal(signal):
    pattern = [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]  # Define the pattern to search for
    start_index = find_start_of_pattern(signal, pattern)
    print(start_index)
    start_index = start_index - 18
    
    if start_index != -1:
        print('start found')
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
# 
# from machine import Pin
# import utime
# 
# from machine import Pin
# import utime
# from machine import Pin
# 
# 
# def read_after_starting_sequence(pin, starting_sequence, sample_rate_us):
#     sequence_to_detect = [1,1,0, 1, 0, 1, 0,1,0,1,0,1,0,1,0,1,0]  # Sequence to detect: alternating high and low
# 
#     while True:
#         readings = []  # Store the sequence of readings
#         for _ in range(len(sequence_to_detect)):
#             readings.append(pin.value())  # Read pin values and store in 'readings'
# 
#         if readings == sequence_to_detect:
#             print("Detected the sequence!")
#             break  # Exit the loop if the sequence is detected
#         if buffer.startswith(starting_sequence):
#             # Perform actions once the starting sequence is detected
#             print("Starting sequence detected!")
#             started_reading = True  # Set flag to start reading
#             buffer_pos = 0  # Reset buffer position
# 
#         if started_reading:
#             # Process or handle the data after the starting sequence is detected
#             # Here, you can add your logic to read or process the incoming data
#             # For example, print the data or trigger specific actions
# 
#             # For demonstration, print the buffer content after starting sequence detection
#             print("Data after starting sequence:", buffer[buffer_pos:])
#             # Add your logic here to process or use the data
#             data_list = buffer[buffer_pos:]
#             transition_indices = find_transition_indices(data_list)
#             transitions_1_to_0 = find_1_to_0_transitions(data_list)
#             
#             delbit, delbitkoord, transition_indices = process_data(data_list, transition_indices, transitions_1_to_0)
#             
#             #print("Delbit:", delbit)
#             #print("Delbitkoord:", delbitkoord)
#             #print("Transition indices:", transition_indices)
#             
#             mes = decode_manchester_signal(delbit)
#             print(mes)
#             avkok = EM410Protocol(mes)
#             print(avkok)
#             
# 
#         utime.sleep_us(sample_rate_us)  # Introduce delay to control sample rate
# 

def main():
    #filename = "readingnone.txt"
    #filename = "readings2_omsparad.txt"
    #filename = "readings3_omsparad.txt"
    #filename = "readings_nymatning.txt"
    filename = "emGOOD.txt"
    
    data_list = read_file(filename)
    transition_indices = find_transition_indices(data_list)
    transitions_1_to_0 = find_1_to_0_transitions(data_list)
    
    delbit, delbitkoord, transition_indices = process_data(data_list, transition_indices, transitions_1_to_0)
    
    print("Delbit:", delbit)
    print("Delbitkoord:", delbitkoord)
    print("Transition indices:", transition_indices)
    
    mes = decode_manchester_signal(delbit)
    print("binart:", mes)
    avkok = EM410Protocol(mes)
    print(avkok)
    

if __name__ == "__main__":
    main()

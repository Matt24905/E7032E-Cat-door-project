# Assuming your file contains values separated by spaces or newlines
with open("BADCUTEM.pm3", "r") as file:
#with open("GoodTestEM410x.pm3", "r") as file:
    values = [int(value) for value in file.read().split()]

# Detect crossings (negative to positive change)
crossings = []
for i in range(1, len(values)):
    if values[i - 1] < 0 and values[i] > 0:
        crossings.append(i)

#print("Crossings occur at indices:", crossings)

Difflength = []
for i in range(1, len(crossings)):
    diff = crossings[i] - crossings[i - 1]
    Difflength.append(diff)
#print(Difflenght)

def median(lst):
    n = len(lst)
    s = sorted(lst)
    return (s[n//2-1]/2.0+s[n//2]/2.0, s[n//2])[n % 2] if n else None

aproxStep = round(median(Difflength))
#print(aproxStep)

# Create a new array starting from the first crossing value + aproxStep
new_array = []
last_value = crossings[-1] + aproxStep  # Calculate the last value using the last crossing point
for i in range(crossings[0], last_value, aproxStep):
    new_array.append(i)

#print("New array:", new_array)

def measure_left_right(values, crossing_index, aproxStep):
    left_index = max(0, crossing_index - aproxStep // 2)
    right_index = min(len(values), crossing_index + aproxStep // 2)
    left_values = values[left_index:crossing_index]
    right_values = values[crossing_index:right_index]
    return 1 if sum(left_values) > sum(right_values) else 0

output_array = []
for crossing in new_array:
    result = measure_left_right(values, crossing, aproxStep)
    output_array.append(result)

print("Output array:", output_array)












def EM410Protocol(output_array):
    # Convert output_array to a string
    output_string = ''.join(map(str, output_array))

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

                # # Uncomment the following lines to print each parity bit
                # even_parity_bit = current_sequence[-1]  # Extract the last bit (parity bit)
                # print(f"5-bit sequence {current_sequence} has even parity bit: {even_parity_bit}")

            else:
                return "Incomplete sequence of 5 bits", ''.join(hex_values)  # Return incomplete sequence error

            start_index += 5  # Move to the next 5-bit sequence

        hex_string = ''.join(hex_values)  # Concatenate the hex values into a single string

        # Calculate column parity for the next 10 sequences (40 bits) with 4 columns
        sequences = [output_string[start_index + i:start_index + i + 5] for i in range(0, 50, 5)]
        columns = [''.join(seq[i] for seq in sequences) for i in range(4)]  # Changed to 4 columns
        column_parity = ''.join('1' if col.count('1') % 2 != 0 else '0' for col in columns)

        # Extract the actual column parity from the output string after the 10 rows
        actual_column_parity = output_string[start_index:start_index + 4]  # Adjust the slicing as needed

        # # Uncomment the following lines to print each column parity and the stop bit
        # print(f"Calculated Column Parity: {column_parity}")
        # print(f"Actual Column Parity: {actual_column_parity}")
        # print(f"Stop bit: {output_string[start_index + 4]}")

        if column_parity == actual_column_parity and output_string[start_index + 4] == '0':
            hex_string = ''.join(hex_values)  # Concatenate the hex values into a single string
            return None, hex_string  # Return None for no errors and the hex string

        else:
            return "Column parity or stop bit mismatch", ''.join(hex_values)  # Return parity or stop bit error

    else:
        return "Header pattern not found", ''  # Return header not found error


# Your previous code remains unchanged up to this point

# Test EM410Protocol function
error_message, hex_string = EM410Protocol(output_array)
if error_message:
    print(error_message)  # Display the error message if any
else:
    print(hex_string)  # Display the hex string if no errors

# Re-run the analysis with the shifted new_array
new_array_shifted = []
for i in range(crossings[0] + (aproxStep // 2), last_value, aproxStep):
    new_array_shifted.append(i)

output_array_shifted = []  # Define output_array_shifted here
for crossing in new_array_shifted:
    result = measure_left_right(values, crossing, aproxStep)
    output_array_shifted.append(result)

print("output_array_shifted:", output_array_shifted)

# Run EM410Protocol function with the shifted output_array
error_message_shifted, hex_string_shifted = EM410Protocol(output_array_shifted)
if error_message_shifted:
    print(error_message_shifted)  # Display the error message if any
else:
    print(hex_string_shifted)  # Display the hex string if no errors

    # if error_message_shifted == "Header pattern not found" or error_message_shifted.startswith("Incomplete sequence of 5 bits"):
    #     print("Shifting again did not find a valid tag.")
    # else:
    #     print("Shifting again found a valid tag.")

# Assuming your file contains values separated by spaces or newlines
with open("GoodTestEM410x.pm3", "r") as file:
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
        print(f"Header pattern found at index: {start_index}")

        # Move past the header pattern
        start_index += len(header_pattern)

        # Check 5-bit sequences and their even parity 10 times
        for _ in range(10):
            current_sequence = output_string[start_index:start_index + 5]

            if len(current_sequence) == 5:
                ones_count = current_sequence.count('1')
                is_even_parity = ones_count % 2 == 0

                if is_even_parity:
                    print(f"5-bit sequence {current_sequence} has even parity.")
                else:
                    print(f"5-bit sequence {current_sequence} does not have even parity.")
            else:
                print("Incomplete sequence of 5 bits.")
                break

            start_index += 5  # Move to the next 5-bit sequence

        # Calculate column parity for the next 10 sequences (40 bits) with 4 columns
        sequences = [output_string[start_index + i:start_index + i + 5] for i in range(0, 50, 5)]
        columns = [''.join(seq[i] for seq in sequences) for i in range(4)]  # Changed to 4 columns
        column_parity = ''.join('1' if col.count('1') % 2 != 0 else '0' for col in columns)
        print(f"Calculated Column Parity: {column_parity}")  # Print calculated column parity

        # Extract the actual column parity from the output string after the 10 rows
        actual_column_parity = output_string[start_index + 0:start_index + 4]  # Adjust the slicing as needed
        print(f"Actual Column Parity: {actual_column_parity}")  # Print actual column parity

        if column_parity == actual_column_parity:
            print("Column parity matches with the actual value for the other sequence.")
            # Check the stop bit (last bit after column parity)
            stop_bit = output_string[start_index + 4]  # Assuming the stop bit is the last bit after column parity
            if stop_bit == '0':
                print("Stop bit is correct.")
                return True
            else:
                print("Stop bit is incorrect.")
                return False
        else:
            print("Column parity does not match with the actual value for the other sequence.")
            return False

    else:
        print("Header pattern not found in the output.")
        return False

# Test EM410Protocol function
found_header = EM410Protocol(output_array)

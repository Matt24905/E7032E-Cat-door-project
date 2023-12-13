import machine
input_array = '1111111110000011101000000000000000101000100111011111010010100010'
def decode_em4100(array):
    # Assuming the array starts with a 9-bit header followed by 10 groups of 4 data bits and a parity bit.
    # It ends with 4 column parity bits and a stop bit.
    
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

# Decode the given input array
decode_result = decode_em4100(input_array)
print(decode_result)
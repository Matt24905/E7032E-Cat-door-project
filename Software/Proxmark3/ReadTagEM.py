EMBINARY = open("EMBINARY.txt", "r")
#print(EMBINARY.read())


# Define an empty list to store the data
data_list = []
data_list1 = []
# Initialize an empty list to store indices of transitions
transition_indices = []

# Open the file in read mode
with open('EMBINARY.txt', 'r') as file:

    # Read each line of the file
    for line in file:
        # Remove newline characters and split the line into elements
        elements = line.strip().split(',')  # Change the delimiter if needed

        # Convert elements to appropriate data types if necessary
        # For example, converting strings to integers or floats
        converted_elements = [int(elem) for elem in elements]  # Example: Convert strings to integers

        # Append the converted elements to the data list
        data_list.append(converted_elements)
        data_list1.append(converted_elements)

# Print the data list to verify
#print(data_list)

# Iterate through the array starting from the second element
for i in range(1, len(data_list)):
    # Check for transitions between adjacent elements
    if data_list[i] != data_list[i - 1]:
        transition_indices.append(i)

# Print indices where transitions occur
print("Transition indices:", transition_indices)

# Initialize an empty list to store indices of transitions from 1 to 0
transitions_1_to_0 = []
Difflenght = []
Difflenght1 = []
# Iterate through the array starting from the second element
for i in range(1, len(data_list1)):
    # Check for transitions from 1 to 0
    if data_list1[i - 1][0] == 1 and data_list1[i][0] == 0:
        transitions_1_to_0.append(i)

# Print indices where transitions from 1 to 0 occur
#print("Transitions from 1 to 0:", transitions_1_to_0)

for i in range(1, len(transitions_1_to_0)):
   Difflenght = transitions_1_to_0[i] - transitions_1_to_0[i - 1]
  # print(Difflenght)

def median(lst):
    n = len(lst)
    s = sorted(lst)
    return (s[n//2-1]/2.0+s[n//2]/2.0, s[n//2])[n % 2] if n else None


for i in range(1, len(transition_indices)):
    diff = transition_indices[i] - transition_indices[i - 1]
    Difflenght1.append(diff)
#print(Difflenght1)

#udda lösning, tar bort korta steg, vilket orsakas av att den är "hög" för länge
aproxStep = round(median(Difflenght1)*1.15)
#print(aproxStep)
#print(data_list)

transistionCounter = 0
delbit = []
delbitkoord = []
i = 0
data_list = [item for sublist in data_list for item in sublist]
while i < len(data_list):
    segment_start = i
    #om vi har passerat en övergång
    if segment_start >= transition_indices[transistionCounter]:
        segment_start = transition_indices[transistionCounter]
        transistionCounter = transistionCounter + 1
    segment_end = segment_start + aproxStep
    #print(data_list[segment_start:segment_end])
    segment_data = sum(data_list[segment_start:segment_end])
    #print(segment_data)
    segment_data = segment_data/aproxStep
    if segment_end > len(data_list):
        break
    
    i = segment_end
    delbitkoord.append(segment_start)

    if segment_data > 0.4:
        delbit.append(1)
    else: 
        delbit.append(0)

print(delbit)
print(delbitkoord)
print(transition_indices)


# analogTOhighlow()
#     #hitta 0 korsningar O
#     #kolla avståndet, dyker upp i multiplar av minsta O
#     #
#     010101010101010110101
#     1 1 1 1 1 1 1 1 0 0 0 0
# highlowTObinary_manchester()



# demanchestercoder ()0101000010-> 11000

# data[480] 111111111111000000000001111111111

# data[480] +32 = 1
# data[480] -32 = 0
# << 1

# data []
# Sample array representing a sequence of 0s and 1s
data_array = [0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1]

# Initialize an empty list to store indices of transitions from 1 to 0
transitions_1_to_0 = []

# Iterate through the array starting from the second element
for i in range(1, len(data_array)):
    # Check for transitions from 1 to 0
    if data_array[i - 1] == 1 and data_array[i] == 0:
        transitions_1_to_0.append(i)

# Print indices where transitions from 1 to 0 occur
print("Transitions from 1 to 0:", transitions_1_to_0)

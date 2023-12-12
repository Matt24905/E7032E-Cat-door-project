# Read the values from the file
with open('GoodTestEM410x.pm3', 'r') as file:
    analog_values = file.readlines()

# Convert analog values to 1 or 0
converted_values = []
for value in analog_values:
    numeric_value = int(value)
    if numeric_value >= 0:
        converted_values.append(1)
    else:
        converted_values.append(0)

# Write the converted values to a new file
with open('converted_values.txt', 'w') as file:
    for value in converted_values:
        file.write(str(value) + '\n')

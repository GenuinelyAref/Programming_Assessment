# Component 2A: First set of questions on rounding

import random

unrounded_number = []
decimal = ""

# Choose the length of the decimal
rand_length = random.randint(2, 8)
# Choose where the decimal point goes (decimal partition)
rand_partition = random.randint(0, rand_length-1)

# Chooses the numbers in the decimal (randomly)
for i in range(0, rand_length):
    unrounded_number.append(random.randint(1, 9))
# Insert the decimal place at the previously chosen random partition
unrounded_number.insert(rand_partition, ".")

# If the decimal number starts with a decimal point (eg:".8456") add a zero ("0.8456")
if unrounded_number[0] == ".":
    unrounded_number.insert(0, 0)

# "Assemble" the decimal number, using the values in the list (decimal point + numbers were generated in a list)
for item in range(0, len(unrounded_number)):
    decimal += str(unrounded_number[item])

# Print the decimal
print(decimal)

# gives the index of the last item in the list
index_length = len(unrounded_number) - 1
# gives the index of the decimal point (".")
index = unrounded_number.index(".")

# give the number of decimal places (number of digits after the decimal point)
decimal_places = index_length - index
print(decimal_places)

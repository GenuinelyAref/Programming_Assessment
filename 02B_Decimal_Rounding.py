# Component 2B: Round decimal

# Random module
import random
# Precise decimal rounding module
from decimal import Decimal

# Manually set decimal
decimal = "34.198643298172346812564"
decimal_list = []

# Set each character (number/decimal point) as an individual item in a list
for i in range(0, len(decimal)):
    decimal_list.append(decimal[i])

# Find the location of the decimal point
decimal_index = decimal_list.index(".")
# Find how many decimal places the decimal has (depending on length of decimal and index of decimal point)
decimal_places = len(decimal_list) - 1 - decimal_index
# Generate a random decimal place to round to between 1 and the actual number of decimal places in the decimal
rounding_dp = random.randint(1, decimal_places-1)
# Capitalised decimal = code from module AND lowercase decimal = actual variable storing decimal
num = Decimal(decimal)
rounded_decimal = round(num, rounding_dp)

print("The decimal {} has {} decimal places".format(decimal, decimal_places))
print("Rounding it to {} decimal places gives {}".format(rounding_dp, rounded_decimal))

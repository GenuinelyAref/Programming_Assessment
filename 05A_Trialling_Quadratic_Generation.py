# Component 5A: --- TRIALLING ---

# To do
# Make a function that returns a non-zero value between
# Generate a complete quadratic factor using one function
# Minimise extra unnecessary code

import random


# Function that generates a non-zero number between a given range
def make_non_zero_num(minimum, maximum):
    number = 0
    while number == 0:
        number = random.randint(minimum, maximum)
    return number


# Function that creates a single quadratic factor, without the brackets involved in the real-life notation
def create_factor(horizontal_shift):
    if horizontal_shift == 0:
        factor = "x"
    elif horizontal_shift > 0:
        factor = "x + {}".format(horizontal_shift)
    else:
        factor = "x - {}".format(-horizontal_shift)
    return factor


# Function that adds x^2 coefficient (if any) to the factor
def add_coefficient(factor, coefficient):
    if coefficient == "none":
        return factor
    elif coefficient == 1:
        return [1, factor]
    elif coefficient == -1:
        factor = "{}{}".format("-", factor)
    elif coefficient != 1:
        factor = "{}{}".format(coefficient, factor)
    return [coefficient, factor]


# Function that adds brackets to a quadratic factor
def add_brackets(factor):
    factor = "({})".format(factor)
    return factor


# Neatly display quadratic (minus/plus signs properly aligned)
def assemble_quadratic(a, b, c):
    part_one = ""
    part_two = ""
    if a == 1:
        part_one = "x\u00b2 "
    elif a == -1:
        part_one = "-x\u00b2 "
    elif a != 1 and a != -1:
        part_one = "{}x\u00b2 ".format(a)
    if b == 0:
        part_two = ""
    elif b == 1:
        part_two = "+ x "
    elif b == -1:
        part_two = "- x "
    elif b < 0 and b != -1:
        part_two = "- {}x ".format(-b)
    elif b > 0 and b != 1:
        part_two = "+ {}x ".format(b)
    if c == 0:
        part_three = ""
    elif c > 0:
        part_three = "+ {}".format(c)
    else:
        part_three = "- {}".format(-c)
    return part_one + part_two + part_three


# Generate numbers used in quadratic equation (horizontal shift & x^2 squared coefficient)
alpha = random.randint(-6, 6)
beta = random.randint(-12, 12)
coefficient_one = make_non_zero_num(-4, 4)
coefficient_two = make_non_zero_num(-2, 2)

# Create quadratic factors
factor_one_details = add_coefficient(create_factor(alpha), coefficient_one)
factor_two_details = add_coefficient(create_factor(beta), coefficient_two)

# Add brackets to the factors
factor_one = add_brackets(factor_one_details[1])
factor_two = add_brackets(factor_two_details[1])

# Print results
print("Alpha = {}\nBeta = {}\nFactor one: {}\nFactor two: {}".format(alpha, beta, factor_one, factor_two))
print("\nQuadratic equation = {}{}".format(factor_one, factor_two))

# Expansion of quadratic equation
a_value = factor_one_details[0] * factor_two_details[0]
b_value = alpha*factor_two_details[0] + beta*factor_one_details[0]
c_value = alpha * beta

# Call function that 'assembles' the quadratic based
expanded_quadratic = assemble_quadratic(a_value, b_value, c_value)

print("\nExpanded quadratic in the form of 'ax\u00b2 + bx + c'")
print("Expanded quadratic = {}".format(expanded_quadratic))

# Calculate roots based on each factor
root_one = -alpha/factor_one_details[0]
root_two = -beta/factor_two_details[0]

print("\nRoot 1: {:.2f}\nRoot 2: {:.2f}".format(root_one, root_two))

# Component 6D: Tricky substitution (exponential equations)

# Equation ==> y = an^(bx+c) + d
# Mathematical limitations:
# >>> a != 0 & n != 0 & b != 0

import random
from sympy import pretty_print as pp
from sympy.abc import x


def make_non_zero_num(low, high):
    val = 0
    while val == 0:
        val = random.randint(low, high)
    return val


# Base of power x
n_value = make_non_zero_num(-4, 4)
while n_value == 1 or n_value == -1:
    n_value = make_non_zero_num(-4, 4)


# Constant after x
c_value = make_non_zero_num(-3, 3)
while c_value == 1 or c_value == -1:
    c_value = make_non_zero_num(-3, 3)

# Vertical shift
d_value = random.randint(-10, 10)

# Base of the function of x
n_value = random.randint(2, 3)

c = c_value
d = d_value
n = n_value

x_value = random.randint(-c_value, 4 - c_value)

solution = (n_value**(x_value + c_value)) + d_value

equation = n**(x + c) + d
print("Solve the following exponential equation for x = {}.\n\n".format(x_value))
pp(equation)
print("\nSolution: {}".format(solution))

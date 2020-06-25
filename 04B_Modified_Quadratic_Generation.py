# Component 4B: Expanding quadratic equation

import random

roots = []
factors = []
coefficient_probability = [-5, -4, -4, -3, -3, -2, -2, -2, -1, -1, -1, -1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 6]

coefficient_one = random.choice(coefficient_probability)
print(coefficient_one)


def generate_roots(variable):
    if variable == 0:
        factor = "x"
    elif variable < 0:
        factor = "(x - {})".format(0-variable)
    else:
        factor = "(x + {})".format(variable)
    roots.append(variable*-1)
    factors.append(factor)
    return factor


def add_coefficient(coefficient):
    string = ""
    for i in range(0, len(root_one)+1):
        try:
            root_one.index("(")
            if i == 0:
                string += str(root_one[0])
            elif i == 1:
                string += str(coefficient)
            else:
                string += str(root_one[i-1])
            print(string)
        except ValueError:
            string = str(coefficient) + root_one
            return string

alpha = random.randint(-12, 12)
root_one = generate_roots(0)

beta = random.randint(-12, 12)
root_two = generate_roots(5)

root_one = add_coefficient(coefficient_one)

print("{}{}".format(root_one, root_two))
print("Solutions are {} and {}".format(roots[0], roots[1]))

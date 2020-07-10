# Component 6A: Basic Substitution

import random

num = 0
expression = ""

while num == 0:
    num = random.randint(-10, 10)

constant = random.randint(-20, 20)
if num == 1 or num == -1:
    while constant == 0:
        constant = random.randint(-20, 20)

x = random.randint(-10, 10)

if num == 1:
    if constant > 0:
        expression = "x + {}".format(constant)
    else:
        expression = "x - {}".format(-constant)
elif num == -1:
    if constant > 0:
        expression = "-x + {}".format(constant)
    else:
        expression = "-x - {}".format(-constant)
else:
    if constant == 0:
        expression = "{}x".format(num)
    elif constant > 0:
        expression = "{}x + {}".format(num, constant)
    else:
        expression = "{}x - {}".format(num, -constant)

print("Expression: {}".format(expression))
print("Substitute and solve for x = {}\n".format(x))

solution = x*num + constant
print("Solution = {}".format(solution))

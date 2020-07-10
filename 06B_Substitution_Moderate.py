# Component 6B: Challenging Substitution

import random


def make_non_zero_num(low, high):
    val = 0
    while val == 0:
        val = random.randint(low, high)
    return val


num = make_non_zero_num(-10, 10)

constant = random.randint(-50, 50)
if num == 1 or num == -1:
    constant = make_non_zero_num(-50, 50)

x = random.randint(-15, 15)

if num == 1:
    if constant > 0:
        expression = "x\u00b2 + {}".format(constant)
    else:
        expression = "x\u00b2 - {}".format(-constant)
elif num == -1:
    if constant > 0:
        expression = "-x\u00b2 + {}".format(constant)
    else:
        expression = "-x\u00b2 - {}".format(-constant)
else:
    if constant == 0:
        expression = "{}x\u00b2".format(num)
    elif constant > 0:
        expression = "{}x\u00b2 + {}".format(num, constant)
    else:
        expression = "{}x\u00b2 - {}".format(num, -constant)

print("Expression: {}".format(expression))
print("Substitute and solve for x = {}\n".format(x))

solution = (x**2)*num + constant
print("Solution = {}".format(solution))

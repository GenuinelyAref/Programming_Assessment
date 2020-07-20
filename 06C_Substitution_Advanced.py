# Component 6C: Tricky Substitution (absolute value)

import random


def make_non_zero_num(low, high):
    val = 0
    while val == 0:
        val = random.randint(low, high)
    return val


def display_coefficients_nicely(position, coefficient, expression):
    if coefficient == 1:
        return expression
    if position != "first":
        if coefficient == 0:
            return ""
        elif coefficient == -1:
            return "- {}".format(expression)
        else:
            if coefficient < 0:
                return "- {}{}".format(-coefficient, expression)
            elif coefficient > 0:
                return "+ {}{}".format(coefficient, expression)
    elif position == "first":
        if coefficient == -1:
            return "-{}".format(expression)
        else:
            return "{}{}".format(coefficient, expression)
    elif position == "fourth":
        if coefficient < 0:
            return "- {}".format(-coefficient)
        elif coefficient == 0:
            return ""
        else:
            return "+ {}".format(coefficient)


num_one = make_non_zero_num(-4, 4)
num_two = make_non_zero_num(-5, 5)
num_three = make_non_zero_num(-3, 3)
num_four = make_non_zero_num(-10, 10)
a = random.randint(-5, 5)
b = random.randint(-6, 6)

answer = num_one*(a**3) + num_two*abs(a-b) + num_three*(b**2) + num_four

part_one = display_coefficients_nicely("first", num_one, "a\u00b3")
part_two = display_coefficients_nicely("second", num_two, "|a - b|")
part_three = display_coefficients_nicely("third", num_three, "b\u00b2")
part_four = display_coefficients_nicely("fourth", num_four, "")

print("{} {} {} {}".format(part_one, part_two, part_three, part_four))

print("a = {} / b = {}".format(a, b))
print("\nSolution: {}".format(answer))

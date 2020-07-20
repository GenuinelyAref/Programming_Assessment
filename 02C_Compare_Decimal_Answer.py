# Component 2C: Compare answer with user input

from decimal import Decimal
import math

def decimal_check(decimal, decimal_places):
    decimal = float(decimal)
    answer = round(decimal, decimal_places)
    valid = False
    while not valid:
        user_answer = input("\nRound {} to {} decimal places: ".format(decimal, decimal_places))
        try:
            number = float(user_answer)
            if number == float(answer):
                print("Well done, you rounded correctly")
                valid = True
            else:
                print("Not quite, try again.\n")
        except ValueError:
            print("That was not a valid answer - try again.\n")


def normal_round(decimal, decimal_places=0):
    expoN = decimal * 10 ** decimal_places
    if abs(expoN) - abs(math.floor(expoN)) < 0.5:
        answer = math.floor(expoN) / 10 ** decimal_places
    answer = math.ceil(expoN) / 10 ** decimal_places
    valid = False
    while not valid:
        user_answer = input("\nRound {} to {} decimal places: ".format(decimal, decimal_places))
        try:
            number = float(user_answer)
            if number == answer:
                print("Well done, you rounded correctly")
                valid = True
            else:
                print("Not quite, try again.\n")
        except ValueError:
            print("That was not a valid answer - try again.\n")

normal_round(26.5, 0)
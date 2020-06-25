# Component 2C: Compare answer with user input

from decimal import Decimal


def decimal_check(decimal, decimal_places):
    answer = round(Decimal(decimal), decimal_places)
    valid = False
    while not valid:
        user_answer = input("Round {} to {} decimal places: ".format(decimal, decimal_places))
        if float(user_answer) == float(answer):
            print("Well done, you rounded correctly")
            valid = True
        else:
            print("Not quite, try again.\n")


decimal_check("42.942453", 3)

# Component 9: Introduction

introduction = "\nThis quiz will be testing you on 4 different areas of mathematics:\n\nRounding decimals\nPythagor" \
               "ean theorem\nQuadratic expansion & solving\nAlgebraic substitution\n\nThere are 3 difficulties to c" \
               "omplete the quiz with, easy, moderate and hard.\nEach difficulty grants you a number of trials for " \
               "each question you complete.\n\nEasy = 5\nModerate = 3\nHard = 1"

print("Welcome to the Y11 Mathematics Quiz!\n")

valid = False
while not valid:
    intro_status = input("Have you used this program before? ")
    if intro_status[0].lower() == "y":
        break
    elif intro_status[0].lower() == "n":
        print(introduction)
        valid = True
    else:
        print("Sorry I don't understand. Please enter either y/yes or n/no\n")

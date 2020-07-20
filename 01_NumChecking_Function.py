# Component 1: Check type of input


def numcheck(value):
    try:
        item = float(value)
        if item % 1 == 0:
            print("You entered an integer")
        else:
            print("You entered a decimal")
    except ValueError:
        print("You entered a string")


# Main routine
for i in range(0, 6):
    user_input = input("\nType a string/float/integer: ")
    numcheck(user_input)

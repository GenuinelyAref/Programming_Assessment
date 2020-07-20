# Y11 Mathematics Quiz


# To do:
# Usability test
# Add feedback from users
# Document changes in documentation slideshow
# Commit changes to GitHub and submit assignment


import random
import math


# General function - Number checking function
def numcheck(value, check_for):
    # check_for = "integer" or "number"
    # if integer, then check modulo 1 value to confirm status of integer
    # else continue with code (doesn't matter if it's an integer or not)
    valid = False
    while not valid:
        try:
            item = float(value)
            # If successful up to this point, then the called "value" is a number
            if check_for == "integer":
                if item % 1 == 0:
                    valid = True
                else:
                    print("You did not enter an integer. Please try again: ")
                    return False
            else:
                valid = True
                return True
        except ValueError:
            # If converting to float gives a ValueError, then called "value" is a string
            print("You did not enter a number, please try again: ")
            return False


# General function - Proper rounding function
def proper_round(decimal, decimal_places):
    expon = float(decimal) * 10 ** decimal_places
    if abs(expon) - abs(math.floor(expon)) < 0.5:
        answer = math.floor(expon) / 10 ** decimal_places
    else:
        answer = math.ceil(expon) / 10 ** decimal_places
    return answer


# General function - Function that generates a non-zero number between a given range
def make_non_zero_num(minimum, maximum):
    number = 0
    while number == 0:
        number = random.randint(minimum, maximum)
    return number


# General function - Text enhancer
def decorate_print(text, char, style):
    # Define used variables
    output = ""
    string = ""
    current_index = 0
    split_text = []
    new_line_index = []

    # Set generic variable values (used in various parts around the function) - really handy, to minimise repeated code
    length = len(text) + 6
    main_line = "{} {} {}".format(2*char, text, 2*char)

    # Type 1 of function: inserts decorative characters on either side of string
    if style == 1:
        output = main_line

    # Type 2 of function: type 1 + 'sandwiching' lines of the decorative character above and below the string
    elif style == 2:
        output = "{}\n{}\n{}".format(length*char, main_line, length*char)

    # Type 3 of function: type 2, but edited to accommodate for \n (line breaks) and centre aligns text on each line
    elif style == 3:
        # Number of \n escape-code characters
        new_lines = text.count("\n")
        # Take indexes of all the \n characters and store them in a list (new_line_index)
        for i in range(0, new_lines):
            if i == 0:
                current_index = text.index("\n")
                new_line_index.append(current_index)
            else:
                new_line_index.append(text.index("\n", current_index+1))
                current_index = new_line_index[i]

        # Take apart parts of string between all the \n, and store each new string as part of a list (split_text), each
        #   to be printed on separate lines in the output

        # Set range of indexes for each run of collecting strings between two '\n's or between one and the end/beginning
        for item in range(0, new_lines+1):
            if item == 0:
                low = 0
                high = new_line_index[0]
            elif item == new_lines:
                low = new_line_index[item-1] + 1
                high = len(text)
            else:
                low = new_line_index[item-1] + 1
                high = new_line_index[item]

            # Collect characters, between indexes set above, and store as one string in a list (split_text)
            for thing in range(low, high):
                string += text[thing]
            split_text.append(string)
            # Reset variable for each group of characters 'extracted' from original string
            string = ""

        # Find longest item in list (split_text), as in the string with most characters
        max_item = max(split_text, key=len)
        # Set the output line for the string with most characters (above)
        max_char_line = "{} {} {}".format(2*char, max_item, 2*char)
        # Length of above output line (used extensively later)
        total_length = len(max_char_line)

        # Top line of decoration
        output += "{}\n".format(total_length*char)

        # Start assembling final output
        for something in range(0, len(split_text)):
            # Avoid re-printing the line that's already been made ready for output above
            if split_text[something] != max_item:
                word = split_text[something]
                # The amount of spacing to put around the string (excluding the normal single space on either side)
                total_spacing = total_length - 6 - len(word)

                # If number of space characters is even, then put half the spaces on each side of string and add 'char'
                if total_spacing % 2 == 0:
                    spaces = int(total_spacing/2)
                    line = "{} {}{}{} {}".format(2*char, " "*spaces, word, " "*spaces, 2*char)
                # If number of space characters is odd, put the extra space on the left side of the string & add 'char'
                else:
                    space = int((total_spacing+1)/2)
                    space2 = space - 1
                    line = "{} {}{}{} {}".format(2*char, " "*space, word, " "*space2, 2*char)
                # Add each line to final output variable
                output += "{}\n".format(line)
            else:
                # Add the longest-string output line to the final output variable
                output += "{}\n".format(max_char_line)

        # Bottom line of decoration
        output += total_length*char

    # After all these hard and tedious, 5+ hours of planning, flow-charting, debugging, crying and typing the code,
    #  print the beautiful outcome, that will HOPEFULLY  work as expected :))
    return output


# Decimal rounding  - answer checking function
def decimal_check(decimal, decimal_places):
    trials = TRIALS
    expoN = float(decimal) * 10 ** decimal_places
    if abs(expoN) - abs(math.floor(expoN)) < 0.5:
        answer = math.floor(expoN) / 10 ** decimal_places
    else:
        answer = math.ceil(expoN) / 10 ** decimal_places
    valid = False
    while not valid:

        if decimal_places == 0:
            user_answer = input("\nRound {} to the nearest whole number: ".format(decimal))
        elif decimal_places == 1:
            user_answer = input("\nRound {} to 1 decimal place: ".format(decimal))
        else:
            user_answer = input("\nRound {} to {} decimal places: ".format(decimal, decimal_places))
        try:
            number = float(user_answer)
            trials -= 1
            if number == answer:
                print("Well done, you rounded correctly")
                round_trials.append(TRIALS - trials)
                valid = True
            else:
                if trials == 0:
                    print("Sorry, that's incorrect. You ran out of trials >> next question")
                    round_trials.append(TRIALS + 1)
                    valid = True
                else:
                    print("Not quite - you have {} trials left. Try again: \n".format(trials))
        except ValueError:
            print("That was not a valid answer - try again: \n".format(trials))


# Quadratic equations - function that creates a single quadratic factor, without the brackets
def create_factor(horizontal_shift):
    if horizontal_shift == 0:
        factor = "x"
    elif horizontal_shift > 0:
        factor = "x + {}".format(horizontal_shift)
    else:
        factor = "x - {}".format(-horizontal_shift)
    return factor


# Quadratic equations - Function that adds x^2 coefficient (if any) to the factor
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


# Quadratic equations - Function that adds brackets to a quadratic factor
def add_brackets(factor):
    factor = "({})".format(factor)
    return factor


# Quadratic equations - Neatly display quadratic (minus/plus signs properly aligned)
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


# Quadratic equations - Function to check if roots are correct
def check_roots(quadratic, first_root, second_root):
    if first_root == second_root:
        question = "\n{} has one (repeated) root, {}. Did you get that answer?\nEnter yes/y if you " \
                   "did or no/n if you didn't - please be honest : ".format(quadratic, first_root)
    else:
        question = "\nThe roots for {} are {} and {}. Did you get that answer?\nEnter yes/y if you did or no/n" \
                   " if you didn't - please be honest: ".format(quadratic, first_root, second_root)
    input("\nWork out the roots for the quadratic equation {}\nAfter"
          " you are done, push any key to check your answer: ".format(quadratic))
    user_input = input(question)
    while user_input.lower() != "yes" and user_input.lower() != "y" and user_input.lower() != "no"\
            and user_input.lower() != "n":
        print("\n{}\n".format("Sorry, I didn't get that. Please try again: "))
        user_input = input(question)
    if user_input[0].lower() == "y":
        print("\n{}\n".format(decorate_print("\U0001F642 \U0001F642 Good job! Next questi"
                                             "on \U0001F642 \U0001F642", "*", 2)))
        round_trials.append(1)
    else:
        print("\n{}\n".format(decorate_print("\U0001F641 \U0001F641 Sorry, you got that wr"
                                             "ong >>> next question \U0001F641 \U0001F641", "!", 2)))
        round_trials.append(TRIALS+1)


# Define all lists used:
unrounded_number = []
round_trials = []
score = []

# Define all variables used:
decimal = ""
question = 0
TRIALS = 5

# - - - - - MAIN ROUTINE STARTS HERE - - - - -


# Introduction:

sections = decorate_print("Rounding decimals\nPythagorean theorem (removed)\nQuadratic expansion & solving\n"
                          "Algebraic substitution (removed)", "-", 3)

introduction = "\nThis quiz will be testing you on 2 different areas of mathematics:\n\n{}\n\n" \
               "You will be given a percentage score on each question, section and an overall\naverage " \
               "performance score at the end. You need a pen & paper for some of the questions.\nYou have 5 trials" \
               " to answer each question. Off you go :)".format(sections)

print(decorate_print("Welcome to the Y11 Mathematics Quiz!", "*", 2))
print("\n")

# If user has used program before don't show introduction
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

print("\n")
# Divider to show where introduction ends and quiz starts
print(decorate_print("> >> Quiz starts here << <", "=", 2))
print()


# Decimal section of quiz...

# Repeat decimal questions 5 times
for i2 in range(0, 5):
    question += 1
    print("\n{}\n".format(decorate_print("Question {}".format(question), ":", 2)))
    unrounded_number = []
    decimal = ""
    # Choose the length of the decimal
    rand_length = random.randint(2, 8)
    # Choose where the decimal point goes (decimal partition)
    rand_partition = random.randint(0, rand_length-1)

    # Chooses the numbers in the decimal (randomly)
    for i in range(0, rand_length):
        unrounded_number.append(random.randint(1, 9))
    # Insert the decimal place at the previously chosen random partition
    unrounded_number.insert(rand_partition, ".")

    # If the decimal number starts with a decimal point (eg:".8456") add a zero ("0.8456")
    if unrounded_number[0] == ".":
        unrounded_number.insert(0, 0)

    # "Assemble" the decimal number, using the values in the list (decimal point + numbers were generated in a list)
    for item in range(0, len(unrounded_number)):
        decimal += str(unrounded_number[item])

    # gives the index of the last item in the list
    index_length = len(unrounded_number) - 1
    # gives the index of the decimal point (".")
    index = unrounded_number.index(".")

    # give the number of decimal places (number of digits after the decimal point)
    decimal_places = index_length - index

    # Generate random dp to round to
    rounding_dp = random.randint(0, decimal_places-1)

    decimal_check(decimal, rounding_dp)


# Quadratics section of quiz...

# Repeat quadratic questions 10 times
for i3 in range(0, 10):
    question += 1
    print("\n{}\n".format(decorate_print("Question {}".format(question), ":", 2)))
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

    # Expansion of quadratic equation
    a_value = factor_one_details[0] * factor_two_details[0]
    b_value = alpha*factor_two_details[0] + beta*factor_one_details[0]
    c_value = alpha * beta

    # Calculate roots based on each factor
    root_one = proper_round(-alpha/factor_one_details[0], 2)
    root_two = proper_round(-beta/factor_two_details[0], 2)

    # Call function that 'assembles' the quadratic based
    expanded_quadratic = assemble_quadratic(a_value, b_value, c_value)

    print(">>> y = {}".format(expanded_quadratic))
    check_roots(expanded_quadratic, root_one, root_two)


# Print out score for each question
for item in range(0, len(round_trials)):
    round_score = (round_trials[item]*-20)+120
    score.append(round_score)
    print("Question {} performance: {}%".format(item+1, round_score))

# Find total average score
average_score = sum(score)/len(score)
# Print it
print("\nOverall performance: {:.1f}%".format(average_score))
# Farewell message
print("\nThank you for completing this quiz")

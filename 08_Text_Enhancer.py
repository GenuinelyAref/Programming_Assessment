# Component 8: Text Enhancer

""" Disclaimer: This code is inspired by Miss Gottschalk, who provided a skeleton to start working on and
gave me the challenge of creating a statement generator function that can decorate multi-line strings. I am
very VERY proud of this piece of code, and consider it a great milestone in my programming journey, which
surprisingly I have explored quite a few of during the completion of this assessment. This program has
required a very great deal of logical and critical thinking, as well as problem analysis. It's easy to
underestimate the ease of which one can code such program, but I can definitely say that this was NOT a
walk-in-the-park type of accomplishment. To be honest too, I consider this program a bigger milestone
than being able to do Level 3 Calculus this year (or maybe I'm just a tad bit too excited haha)

HOW TO USE PROGRAM:

1) First, explore the different function capabilities by running the code
2) Go all the way to the bottom of the code, and play around

WHAT YOU CAN DO:

I) Change the number of '\n's
II) Change the length of different terms/words between the '\n's
III) (Do at own risk of crashing program) Change the mode/style (third parameter of function) and have fun
IV) Suggest where I can take this from to improve it (generally) and provide insight on how to use this successfully
in the final quiz program

"""


# Function that takes any string (single line/multi-line) and returns it, printed with a decorative character and
#    using clean indentation
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


# Type 1 testing, winning message, single line decoration
win = decorate_print("Correct!", "-", 1)
# Type 2 testing, losing message, triple line decoration
loss = decorate_print("Sorry, that's incorrect", ":", 2)
# Type 3 testing, very happy message!!, multi-line (3+) decoration
test = decorate_print("My\nprogram\nworks\nas\nexpected,\nyay!!", "*", 3)

# Print the returned values within the variables
print("{}\n\n{}\n\n{}".format(win, loss, test))

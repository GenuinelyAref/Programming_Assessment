# Component 7A: Score Mechanics

questions = ["What city is the Sky Tower in? ", "When did WWI start? ", "What is Miss Gottschalk's class code? ",
             "What is the last name of the principal at MHS? ", "How many NCEA L1 credits does a Year 11 student"
                                                                " typically need to pass the year? "]

answers = ["auckland", "1914", "c206", "denham", "80"]

for i in range(0, 5):
    answer = input("Question {}: {}".format(i+1, questions[i])).lower()
    if answer == answers[i]:
        print("That's correct!\n")
    else:
        print("Sorry that's incorrect :(\n")
        print("Your answer: {}\tCorrect answer: {}".format(answer, answers[i]))

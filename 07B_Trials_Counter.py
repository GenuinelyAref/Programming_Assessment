# Component 7B: Trials counter

questions = ["name: ", "age: ", "school: ", "year: ", "favourite colour: "]
answers = ["aref", "15", "mhs", "11", "red"]
round_trials = []
question = 0
TRIALS = 5

for i in range(0, len(questions)):
    trials = TRIALS
    question += 1
    print("\nQuestion {}".format(question))
    valid = False
    while not valid:
        user_input = input(questions[i])
        trials -= 1
        if user_input == answers[i]:
            print("Correct! ")
            round_trials.append(TRIALS - trials)
            break
        else:
            valid = False
            if trials == 0:
                print("Sorry, that's incorrect. You ran out of trials >> next question")
                round_trials.append(TRIALS - trials)
                break
            else:
                print("Sorry, that's incorrect (you have {} trial(s) left)".format(trials))


print("\n")

for item in range(0, len(questions)):
    print("You took {} trial(s) for question {}".format(round_trials[item], item+1))

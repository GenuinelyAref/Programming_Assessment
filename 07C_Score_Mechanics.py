# Component 7C: Score mechanics

# Score will be displayed as a percentage of mastery from 0% to 100%
# Getting the answer on the first guess gives 100% score
# Not getting the answer in the number of given trials gives 0% score
# Getting the answer in more than one guess gives an evenly distributed score percentage (factor of 25 - for 5 trials)

questions = ["name: ", "age: ", "school: ", "year: ", "favourite colour: "]
answers = ["aref", "15", "mhs", "11", "red"]
round_trials = []
score = []
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
                round_trials.append(TRIALS+1)
                break
            else:
                print("Sorry, that's incorrect (you have {} trial(s) left)".format(trials))
    print(round_trials)
print()
for item in range(0, len(questions)):
    round_score = (round_trials[item]*-20)+120
    score.append(round_score)
    print("Question {} performance: {}%".format(item+1, round_score))

average_score = sum(score)/len(score)
print("Overall performance: {:.0f}%".format(average_score))

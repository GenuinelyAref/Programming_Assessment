# Component 7A: Round counter

questions = ["name: ", "age: ", "school: ", "year: ", "favourite colour: "]
question = 0

for i in range(0, len(questions)):
    question += 1
    print("\nQuestion {}".format(question))
    user_input = input(questions[i])

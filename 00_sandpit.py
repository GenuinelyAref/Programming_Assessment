def thing(question):
    ask = int(input(question))
    return [ask, "hello"]


rounds = thing("write a number")
number = rounds[0]
greeting = rounds[1]

print(rounds)

print("{} - {} is the best number".format(greeting, number))

# Task 1: Loop Condition Exploration

while True:
    bball_player = input("who's your favorite basketball player? ")

    if bball_player == 'Jordan':
        print('That is the correct answer. Enjoy the game!')
        break
    else:
        print("WRONG ANSWER TRY AGAIN")


# Task 2: Conditional Exit 

age = 5

while age <= 25:
    print(age, 'I can still play soccer!!!')
    age += 5
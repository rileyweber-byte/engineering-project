import random
# defines random integer
def my_random_number():
    return random.randint(1,12)
# starts a function to where my random number when stated 
def dealers_turn():
    return random.randint(1, 12)
# when it is the dealers turn, i will use this variable which is defined as a random integer
def end_of_game_question():
    return print(input("Do you want to play again? (Say Yes or No) "))
# this will help end my while true loop once the game is over

while True:
    player = input("Player's name? ")
    print("Hello, "+player)
    dealer = input("Dealer's name? ")
    print("Hello, "+dealer)
    rando = my_random_number()
    end_of_game = end_of_game_question()
    dealerscard = dealers_turn()
    print("First it is " +player+ "s turn")
    print(rando)
    while True:
        x = input("Do you want to stay or go? ")
        if x == "go":
            rando += random.randint(1,12)
            print(rando)
        elif x == "stay":
            break
        if rando == 21:
            print("You Win!")
            break
    if rando > 21:
        print("You Went Over 21 You Lose!")
        break
    print(end_of_game)
    if end_of_game == "Yes":  
        continue
    if end_of_game == "No":
        print("Ok! Have an amzing day!")
    print("Now it is "+dealer+"s turn")
    print(dealerscard)
    while True:
        y = input("Do you want to stay or go? ")
        if y == "go":
            dealerscard += random.randint(1,12)
            print(dealerscard)
        if dealerscard == 21 and dealerscard == rando:
            print("You tie!")
            break
        if dealerscard > 21:
            print("Player Wins!")
            break
        if dealerscard < 21 and dealerscard > rando:
            print("Dealer Wins!")
            break
    print(end_of_game)
    if end_of_game == "Yes":  
        continue
    if end_of_game == "No":
        print("Ok! Have an amzing day!")
        
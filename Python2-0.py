import random
# defines random integer
def my_random_number():
    return random.randint(1,12)
# starts a function to where my random number when stated 
def dealers_turn():
    return random.randint(1, 12)
# when it is the dealers turn, i will use this variable which is defined as a random integer
def end_of_game_question():
    return input("Do you want to play again? (Say yes or no) ").lower()
# this will help end my while true loop once the game is over

while True:
# makes it an infinite loop unless a break statment is specified
    player = input("Player's name? ")
# this identifies what the player's name is
    print("Hello, "+player)
    dealer = input("Dealer's name? ")
# identifies the dealer's name
    print("Hello, "+dealer)
    rando = my_random_number()
# calls the function i made for a random integer 1-12 for the player
    dealerscard = dealers_turn()
# calls the function i made for a random integer 1-12 for the dealer
    print("First it is " +player+ "s turn")
    print(rando)
# starts the turn for player
    while True:
# nested while loop, so if the game ends I can back out of of the loop or continue the loop
        x = input("Do you want to stay or go? (say stay or go) ").lower()
        if x == "go":
            rando += random.randint(1,12) # adds another random number to the already printed random number
            print(rando)
        elif x == "stay":
            break # breaks the loop and goes to the next turn
        elif x != "stay" or "go": # makes you put either stay or go
            print("Please, put either stay or go!")
            continue
        if rando == 21: # win if statement
            print("You Win!")
            break
        if rando > 21: # lose if statement
            print("You Went Over 21 You Lose!")
            break
    end_of_game = "" # empty string to call end_of_game
    while rando > 21 or rando == 21: # another nested while loop
        end_of_game = end_of_game_question()
        if end_of_game == "yes":
            break
        elif end_of_game == "no":
            print("Ok! Have an amazing day!")
            break
        elif end_of_game != "yes" or "no":
            print("That is not yes or no. Please try again!")
            continue
    if end_of_game == "no": # ends game officially
        break
    if end_of_game == "yes": # restarts game entirely
        continue
# this now starts the dealer's turn
    print("Now it is "+dealer+"s turn")
    print(dealerscard)
    while True: # the dealer's nested while loop 
        y = input("Do you want to stay or go? (say stay or go) ").lower()
        if y == "go":
            dealerscard += random.randint(1,12) # adds on a random integer 1-12 to the dealer's number
            print(dealerscard)
        if y == "stay":
            print("The dealer cannot stay! Please type go! ")
        if dealerscard == 21 and dealerscard == rando: # tie if statement
            print("You tie!")
            break
        if dealerscard > 21: # player wins if statement
            print("Player Wins!")
            break
        if dealerscard < 21 and dealerscard > rando: # dealer wins if statement
            print("Dealer Wins!")
            break
    end_of_game = "" # another empty string so it calls end_of_game
    while dealerscard > 21 or dealerscard == 21 and dealerscard == rando or dealerscard < 21 and dealerscard > rando:
        end_of_game = end_of_game_question()
        if end_of_game == "yes": 
            break
        elif end_of_game == "no":
            print("Ok! Have an amazing day!")
            break
        elif end_of_game != "yes" or "no":
            print("That is not Yes or No. Please try again!")
            continue
    if end_of_game == "no": # ends the game
        break
    if end_of_game == "yes": # restarts the game
        continue

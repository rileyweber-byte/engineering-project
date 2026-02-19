# Engineering_21_Game
I want my code to create a game of 21 with players defined aas dealer and other players. I want it to be able to tell when I win or lose.


MY CODE:
import random
def my_random_number():
    return random.randint(1,12)
player = input("Your name? ")
print("Hello, "+player)
rando = my_random_number()
print(my_random_number())
while my_random_number() < 21: 
    x = input("Do you want to stay or go? ")
    if x == "go":
        rando += random.randint(1,12)
        print(rando)
        if rando == 21:
            print("You Win!")
            break
        if rando > 21:
            print("You Went Over 21 You Lose!")
            break

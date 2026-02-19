# Engineering_21_Game
What do I want my code to do? 
I want my code to create a game of 21 with players defined as a dealer and how ever many other players are playing. I want it to be able to tell when I win or lose while being able to swtch between players turns. I want to use a random number generator 1-12 to act as if I'm drawing cards in real life. I want to mastr the while loop with user inputs as well. Lastly, I want to define my own functions for my code and call every one I make.
What does my code currently do?
My code currently starts by defining a function which is my random number generator 1-12. It then asks for player's input on what is your name. It then repsonds back by saying hello (name). It then creates a variable with my function I created earlier, and it prints that function as a integer. Then, I created a while loop for when my random number is less than 21. Everytime it is, I ask whether the player wants to stay or go.


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

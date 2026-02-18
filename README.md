# engineering-project
This is my github file for my engineering project which I have no idea what is going to be yet. I will make something awesome and cool for my engineering project.
MY CODE:
import random
def my_random_number():
    return random.randint(1,12)
player = input("Your name? ")
print("Hello, "+player)
rando = my_random_number()
print(my_random_number())
while True: 
    x = input("Do you want to stay or go? ")
    if x == "go":
        rando += random.randint(1,12)
        print(rando)
        if rando == 21:
            print("You Win!")

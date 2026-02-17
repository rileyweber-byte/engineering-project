# engineering-project
This is my github file for my engineering project which I have no idea what is going to be yet. I will make something awesome and cool for my engineering project.

My Code:
import random
def my_random_number():
    print(random.randint(1,12))
my_random_number_1 = random.randint(1,12)
my_random_number_2 = random.randint(1,12)
player = input("Your name? ")
print("Hello, "+player)
print(my_random_number)
while True: 
    x = input("Do you want to stay or go? ")
    if x == "go":
        print(my_random_number + my_random_number_1)
    while x != "stay":
        x = input("Do you want to stay or go? ")

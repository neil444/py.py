import random
n=input=("guess a number between 1 and 9")
number = random.randint(1, 9)
chances=5
while chances < 5:
    if n==number:
        print("you won !!!!!!!!!!!")
        break
    if not chances<5:
        print("you lost  the num ber is" + number)
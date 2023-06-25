import random

def roll_dice(n):
    for i in range(n):
        a = random.randint(1,6)
        print(a,end = " ")

while True:
    
    diceNumber = int(input("Number of dice do you want to roll (more than 2:) "))
    roll_dice(diceNumber)
    print()

    s = input("Do you want roll dice again (Y/N) : ")
    if s.lower() == "y":
        continue
    else:
        break

import random

print("-----------------------------------")
print("  WELCOME TO NUMBER GUSIING  GAME  ")
print("-----------------------------------")
name = input("Please enter your name:  ")
number = random.randint(1,100)
print("Guuss the number with in 1 to 100")
print("You have only 10 chances to guess the number ")


for i in range(10):
    print("Please enter your ",i+1,"guess")
    guess = int(input())
    if guess == number:
        print("Your guess is correct and you win the game ",name)
        break
    elif(guess <=number+10 and guess>=number-10):
        print("your close to the number")

    else:
        print("your guess is too far away from the number")

    if i<9:
        con = input("Do you want to continue press: 'Y' to Quit press :'N' ")
    
        if con.lower() == "y":
            continue
        else:
            break

print("The real number is :",number)


import random
import os

guess_number = random.randrange(1,9)
user_guess = 0
try_again = ''

print("Guess the number from 1-9.")
while(user_guess != guess_number or try_again == 'Y'):
    user_guess = int(input("Guess the number: "))
    if(user_guess == guess_number):
        print("That is correct!")
        try_again = input("Try Again? [Y/N]: ")
        if(try_again == 'Y'):
            os.system('cls')
            continue
        else:
            break
    else:
        print("Incorrect Number!")
        if(user_guess > guess_number):
            print("Hint: The number is lower")
            continue
        elif(user_guess < guess_number):
            print("Hint: The number is higher")
            continue
        else:
            print("Incorrect Input!")
            continue
import random as rd
import os

try_again_input = 'Y'
try_again = True
while(try_again_input == 'Y'):
    print("ROCK PAPER SCISSORS!")
    user = input("Enter Choice: ")
    cpu_player = ['ROCK','PAPER','SCISSORS']
    cpu_choice = rd.choice(cpu_player)

    print("CPU Picks: " + cpu_choice)

    if(user == "ROCK"):
        if(cpu_choice == "ROCK"):
            print("DRAW!")
        elif(cpu_choice == "PAPER"):
            print("YOU LOSE!")
        elif(cpu_choice == "SCISSORS"):
            print("YOU WIN!")
    elif(user == "PAPER"):
        if(cpu_choice == "ROCK"):
            print("YOU WIN!")
        elif(cpu_choice == "PAPER"):
            print("DRAW!")
        elif(cpu_choice == "SCISSORS"):
            print("YOU LOSE!")
    elif(user == "SCISSORS"):
        if(cpu_choice == "ROCK"):
            print("YOU LOSE!")
        elif(cpu_choice == "PAPER"):
            print("YOU WIN!")
        elif(cpu_choice == "SCISSORS"):
            print("DRAW!")
    else:
        print("ERROR! TRY AGAIN!")
    try_again_input = input("Try Again? [Y/N]: ")
    if try_again_input == 'Y':
        os.system('cls')
        continue
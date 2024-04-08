guess = input("Enter a number and the program will tell if its odd or even: ")
program_guess = int(guess) % 2

if(program_guess == 0):
    print("This is an even number")
else:
    print("This is an odd number")
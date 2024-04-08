x = range(2,11)
guess = int(input("Enter number here: "))

for i in x:
    c = guess % i
    if (c == 0):
        print(str(guess) + " is divisible by " + str(i))
    else:
        continue
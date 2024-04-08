def AskNumber():
    return int(input("Give a number: "))

number = AskNumber()

for i in range(2, int(number)):
    if number % i == 0:
        print("Not a prime number")
        break
else:
    print("It is a prime number")
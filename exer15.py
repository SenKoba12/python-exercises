
myString = input("Enter your string here: ")


def reverse(stringInput):
    print("Normal: ", stringInput)

    stringRev = stringInput.split()[::-1]
    stringRev = str(stringRev)
    stringRev = stringRev.replace(', ', ' ').replace('[','').replace(']','').replace("'",'')
    print("Reverse: ", stringRev)

reverse(myString)
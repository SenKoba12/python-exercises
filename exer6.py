#PALINDROME
#user inputs word
#to be a palindrome, word must be equal to its reverse/backwards
#if word is not equal to its reverse, it is not a palindrome

word = input("Enter a word: ")
reverse = word[::-1]

if(word == reverse):
    print("This is a palindrome")
else:
    print("Not a palindrome")
import random as rd
import string 
string.ascii_letters
string.punctuation

def generatePass():

    password_list=[]

    for j in range(0, rd.randint(4,5)):
        j = rd.randint(0,100)
        password_list.append(j)
    for i in range(0, rd.randint(4,5)):
        i = rd.choice(string.ascii_letters.replace("'",''))
        password_list.append(i)
    for k in range(0,2):
        k = rd.choice(string.punctuation.replace("'",''))
        password_list.append(k)

    rd.shuffle(password_list)
    password_new = str(password_list)
    password_clean = password_new.replace("'",'').replace('[','').replace(']','').replace(',','').replace(' ','')
    print(password_clean)


def main():
    print("This is your generated password: ")
    generatePass()

if __name__ == '__main__':
    main()
import random as rd

def enterNumber(num):
    generate_num = rd.randrange(1000,10000)
    if(num != generate_num):
        user_conv = [int(y) for y in str(num)]
        num_conv = [int(x) for x in str(generate_num)]
        print("USER INPUT: ")
        print(user_conv)
        print("GENERATED: ")
        print(num_conv)
        i = 0
        counter = 0
        cow = 0
        bull = 0
        combined_list = user_conv + num_conv
        clean = set(combined_list)
        print("COMBINED LIST")
        print(list(clean))


        new_list = list(set(user_conv).intersection(num_conv))
        print("COMMON: ")
        print(new_list)
        while(counter != 4):
            if i in num_conv or i in user_conv:
                if((str(user_conv[i]) != str(num_conv[i]))):
                    cow += 1
                elif(str(user_conv[i]) == str(num_conv[i])):
                    bull +=1
                else:
                    pass  
                i += 1
                counter += 1
            else:
                pass
        print("The number of bulls are: " + str(bull))
        print("The number of cows are: " + str(cow))



if __name__=="__main__":
    guess = int(input("Enter your 4-digit number: "))
    enterNumber(guess)
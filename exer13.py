def fibonacci():
    counter = 0
    enterNum = int(input("Enter numbers to generate: "))
    prev= 0
    curr = 0
    new = 1

    while(counter != enterNum):
        prev = curr
        curr = new
        new = prev + curr
        print(curr)
        counter += 1
        
fibonacci()
        

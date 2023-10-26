def even():
   
    num = int(input("Enter an Integer :"))

    if (num & 1) == 0:
        print( f"{num} is even")
    else:
        print(f"{num} is odd")


even()


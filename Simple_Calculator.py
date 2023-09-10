def add(x, y):
    return x + y

def subt(x, y):
    return x - y

def mul(x, y):
    return x * y

def rem(x,y):
    return x % y

def div(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero is not allowed."
while True:
    print("\nCalculator Program")
    print("------------------")

    print("\nSelect an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("\nInput 5 or greater number to exit program")

    choice = input("Enter your choice : ")
    if choice >= '5':
        break
    elif choice in ('1','2','3','4'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            result = add(num1, num2)
            print("Sum : ", result)
        elif choice == '2':
            result = subt(num1, num2)
            print("Difference : ", result)
        elif choice == '3':
            result = mul(num1, num2)
            print("Product : ", result)
        elif choice == '4':
            result = div(num1, num2)
            result1 = rem(num1, num2)
            print("\nResult : ", result)
            print("Remainder : ", result1)
        
            



import math

def square_root():
    x = int(input("\nEnter your number : "))
    print("\nSquare root of ", x, "is ", math.sqrt(x))
def cube_root():
    x = int(input("\nEnter your number : "))
    print("\nCube root of ", x, "is ", math.cbrt(x))

def factorial():
    x = int(input("\nEnter your number : "))
    print("\nFactorial of ", x, "is", math.factorial(x))

def gcd():
    y = int(input("\nEnter your first number : "))
    z = int(input("Enter your second number : "))
    print("\nGCD of given two numbers is ", math.gcd(y, z))

def lcm():
    y = int(input("\nEnter your first number : "))
    z = int(input("Enter your second number : "))
    print("\nLCM of given two numbers is ", math.lcm(y, z))

def permutations():
    y = int(input("\nEnter the total number of items : "))
    z = int(input("Enter the number of items to choose : "))
    print("\nFrom the given data we choose", z, "items", "in", math.perm(y, z), "ways")

def combinations():
    y = int(input("\nEnter the total number of items : "))
    z = int(input("Enter the number of possibilities to choose : "))
    print("\nFrom the given data total no.of combinations can be done are", math.comb(y, z))

def logarithms():
    y = int(input("\nEnter logarithm : "))
    z = int(input("Enter Base : "))
    print("\nLogarithm of given exponent is", math.log(y, z))


print("1 --> Find Square root")
print("2 --> Find Square root")
print("3 --> Find Factorial")
print("4 --> Find GCD of two numbers")
print("5 --> Find LCM of two numbers")
print("6 --> Find Permutations")
print("7 --> Find Combinations")
print("8 --> Find Logarithms")

choice = int(input("\nEnter your choice : "))

if choice == 1:
    square_root()
elif choice == 2:
    cube_root()
elif choice == 3:
    factorial()
elif choice == 4:
    gcd()
elif choice == 5:
    lcm()
elif choice == 6:
    permutations()
elif choice == 7:
    combinations()
elif choice == 8:
    logarithms()
else:
    exit()

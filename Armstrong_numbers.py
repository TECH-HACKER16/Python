n = int(input("Enter the number : "))

original_number = n
result = 0

while original_number != 0:
    remainder = original_number % 10
    result += remainder ** 3
    original_number //= 10

if result == n:
    print(n, 'is an Armstrong numbers')
else:
    print(n, 'is not an Armstrong number')

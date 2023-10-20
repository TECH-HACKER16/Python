n = int(input("Enter the number of terms required : "))

x = 0
y = 1
print(x)
print(y)

for i in range(2, n):
    z = x+y
    x = y
    y = z
    print(z)
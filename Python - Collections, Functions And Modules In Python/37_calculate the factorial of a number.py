number = int(input("Enter a nonnegative integer : "))

result = 1
for i in range(1, number + 1):
    result *= i

print("The factorial of",number,"is",result)
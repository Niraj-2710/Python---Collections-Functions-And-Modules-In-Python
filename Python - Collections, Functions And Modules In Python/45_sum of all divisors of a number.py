N = int(input("Enter a number : "))
sum_of_divisors = 0
for i in range(1, N + 1):
    if N % i == 0:
        sum_of_divisors += i
print("Sum of divisors :", sum_of_divisors)
def is_perfect(N):
    sum = 0
    for i in range(1, N):
        if N % i == 0:
            sum += i
    return sum == N

print(is_perfect(6))
print(is_perfect(28))
print(is_perfect(5))
print(is_perfect(120))
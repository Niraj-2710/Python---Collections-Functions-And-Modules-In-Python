N1 = float(input("Enter the first number : "))
N2 = float(input("Enter the second number : "))
N3 = float(input("Enter the third number : "))

max_num = N1
min_num = N1

if N2 > max_num:
    max_num = N2
if N2 < min_num:
    min_num = N2

if N3 > max_num:
    max_num = N3
if N3 < min_num:
    min_num = N3

print("Maximum number : ", max_num)
print("Minimum number : ", min_num)
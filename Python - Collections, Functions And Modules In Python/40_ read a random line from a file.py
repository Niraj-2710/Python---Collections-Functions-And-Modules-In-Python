import random

file_path = 'Demo.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

if lines:
    random_line = random.choice(lines)
    print(random_line.strip())
else:
    print("The file is empty....")
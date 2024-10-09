list = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

dictionary = {}

for tuple in list:
    dictionary[tuple[0]] = tuple[1]

print(dictionary)
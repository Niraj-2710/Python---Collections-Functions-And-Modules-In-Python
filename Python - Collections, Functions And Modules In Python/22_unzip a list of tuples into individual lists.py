list = [(1, 'a', 'x'), (2, 'b', 'y'), (3, 'c', 'z')]

list1, list2, list3 = [], [], []

for tuple in list:
    list1.append(tuple[0])
    list2.append(tuple[1])
    list3.append(tuple[2])

print("List 1:", list1)
print("List 2:", list2)
print("List 3:", list3)
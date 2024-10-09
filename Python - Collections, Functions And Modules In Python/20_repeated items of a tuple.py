T = (1, 2, 2, 3, 4, 4, 4, 5, 6 , 6, 7, 8, 8, 9)
print(T)

res = []
for i in T:
    if T.count(i) > 1:
        res.append(i)
    else:
        continue

for x in res:
    while res.count(x) > 1:
        res.remove(x)

print("Repeated items:", tuple(res))
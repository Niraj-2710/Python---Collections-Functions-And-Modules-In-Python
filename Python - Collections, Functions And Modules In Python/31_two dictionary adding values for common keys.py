from collections import Counter

D1 = {'a': 100, 'b': 200, 'c': 300}
D2 = {'a': 300, 'b': 200, 'd': 400}

combined_counter = Counter(D1) + Counter(D2)

print(combined_counter)
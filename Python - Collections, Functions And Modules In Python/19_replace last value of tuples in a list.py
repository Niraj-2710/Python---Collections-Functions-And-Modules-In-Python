L = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

new_tuples_list = [tuple(list(t)[:-1] + [10]) for t in L]

print(new_tuples_list)
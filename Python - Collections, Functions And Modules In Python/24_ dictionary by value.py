example = {'apple': 1, 'banana': 2, 'cherry': 3, 'date': 4, 'elderberry': 5}

sorted_dict_ascending = sorted(example.items(), key=lambda x: x[1])
print("Sorted dictionary in ascending order:")
for key, value in sorted_dict_ascending:
    print(f"{key}: {value}")

sorted_dict_descending = sorted(example.items(), key=lambda x: x[1], reverse=True)
print("\nSorted dictionary in descending order:")
for key, value in sorted_dict_descending:
    print(f"{key}: {value}")
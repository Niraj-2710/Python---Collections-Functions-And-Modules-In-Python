D = {'A': 100, 'B': 200, 'C': 300, 'D': 400, 'E': 500}

keys_to_check = ['A', 'C', 'E']

for key in keys_to_check:
    if key in D:
        print("Key",key,"exists in the dictionary...")
    else:
        print("Key",key,"does not exist in the dictionary...")
def string_to_dict(s):
    C_count = {}
    for char in s:
        if char in C_count:
            C_count[char] += 1
        else:
            C_count[char] = 1
    return C_count

s = 'w3resource'
print(string_to_dict(s))
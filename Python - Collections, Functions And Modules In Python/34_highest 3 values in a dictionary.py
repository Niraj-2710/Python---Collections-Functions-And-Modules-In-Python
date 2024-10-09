D = {"A": 30, "B": 40, "C": 10, "D": 80, "E": 29, "F": 90, "G": 70, "H": 60, "I": 50}

sorted_dict = sorted(D.items(), key=lambda x: x[1], reverse=True)

top_3 = sorted_dict[:3]

result_dict = dict(top_3)

print(result_dict)
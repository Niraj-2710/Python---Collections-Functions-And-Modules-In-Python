Data = [["Name", "rose"], ["age", 28], ["city", "U K"], ["Name", "Rock"], ["age", 30], ["city", "England"]]

unique_values = []

for item in Data:
    if item[1] not in unique_values:
        unique_values.append(item[1])

print("Unique values:")
for value in unique_values:
    print(value)
from collections import Counter

D = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

combined_amounts = {}

for d in D:
    item = d['item']
    amount = d['amount']
    
    if item in combined_amounts:
        combined_amounts[item] += amount
    else:
        combined_amounts[item] = amount

result = Counter(combined_amounts)

print(result) 
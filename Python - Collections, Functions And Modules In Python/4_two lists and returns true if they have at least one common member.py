'''Write a Python function that takes two lists and returns true if they have 
at least one common member.'''

L = [10,20,30]
L2 = [30,40,50]

if set(L) & set(L2):
    print("There is an intersection between the two lists...")
else:
    print("There is no intersection between the two lists...")
    
L = [10,20,30]
L2 = [40,50,60]

if set(L) & set(L2):
    print("The Lists Have At Least One Common Member...")
else:
    print("The Lists Have No Common Members...")
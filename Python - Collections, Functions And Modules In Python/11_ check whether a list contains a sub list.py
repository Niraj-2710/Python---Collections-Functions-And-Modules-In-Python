'''Write a Python program to check whether a list contains a sub list.'''

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
S_L = [3, 4, 5] 

if all(x in L for x in S_L):
    print("The Main List Contains The Sub List...")
else:
    print("The Main List Does Not Contain The Sub List...")
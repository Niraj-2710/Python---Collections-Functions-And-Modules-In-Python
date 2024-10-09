''' Write a Python program to check whether an element exists within a 
tuple '''

T = ("apple", "banana", "charry", "date", "elderberry")

element_to_search = "banana"

if element_to_search in T:
    print(f"The Element {element_to_search} exists in the tuple")
else:
    print(f"The Element {element_to_search} does not exist in the tuple")
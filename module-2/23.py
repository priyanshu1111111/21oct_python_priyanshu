#23. Write a Python function to insert a string in the middle of a string.

a=input("Enter a String: ")

add=input("Enter a string to add string in middle of origional string: ")

x=a.find(" ")

new_str=a[:x] + " " + add + " " + a[x+1: ]

print(new_str)
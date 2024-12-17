#Q22. Write a Python program to get a string made of the first 2 and the last 
#2 chars from a given a string. If the string length is less than 2, return 
#instead of the empty string."""

n=input("Enter  string: ")

length=len(n)

if length < 2:
    print("empty string")
else:
    a=n[:2]
    b=n[-2:]
    str=a + b
    print(str)
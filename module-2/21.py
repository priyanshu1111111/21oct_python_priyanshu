#21. Write a Python function to reverses a string if its length is a multiple of 4.

string=input("Enter  Word: ")

str_length=len(string)

if str_length % 4 == 0:
    print(string[::-1])
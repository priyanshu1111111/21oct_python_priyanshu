 #15. Write a Python program to count occurrences of a substring in a string.

n=input("Enter string for match main string: ")
sen=input("enter main string=")

count=sen.count(f"{n}")

print(f"The substring {n} appears {count} times in the main string.")
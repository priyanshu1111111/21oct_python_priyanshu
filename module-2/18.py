#18. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
#If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is 
#less than 3, leave it unchanged."""

n=input("Enter an any word(length should be at least 3): ")

length=len(n)

if length < 3:
    print(n)
elif n[-3:] == "ing":
    print(n.replace("ing", "ly"))

elif length >= 3:
    print(n + "ing")
    
# 17. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

string="Hello World!"

seprate=string.split()

a=seprate[0]

b=seprate[1]

replace_x=a.replace("He","eh")

replace_y=b.replace("Wo","ow")

print(replace_x)

print(replace_y)
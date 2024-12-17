import re
a=input("Enter your email=")
b="[a-z]+[0-9]+@+[a-z]+.com"
x=re.findall(b,a)
if x:
    print("email valid")
else:
    print("email not valid")
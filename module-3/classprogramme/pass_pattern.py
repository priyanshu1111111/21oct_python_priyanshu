import re
pas=input("Enter password(example=Xyx@123)=")
check="[A-Z]+[a-z]+@|*|.|&|%|$|#|!+[0-9]"
x=re.findall(check,pas)
if x:
    print("yes")
else:
    print("no")

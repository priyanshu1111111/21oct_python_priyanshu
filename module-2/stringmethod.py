print("===============Input======================")

name=input("Enter name=")
age=input("Enter your Age=")
email=input("Enter your email=")
pas=input("Enter your password=")
cpas=input("Enter your confirm password=")
num=input("Enter your mobile number=")

print("=================Output==================")

a=name.isalpha()
if a==True:
    print(f"Name enter sucssesfully")
else:
    print("Name= Error")

b=age.isdigit()
if b==True:
    print(f"Age enter sucessfuly")
else:
    print("Age= Error")

e=email.islower()
if e==True:
    print(f"Email enter sucssefuly")
else:
    print("Email= Error")

if pas==cpas:
    print(f"Password enter sucssesfuly")
else:
    print("Password= Error")

n=num.isdigit()
l=len(num)
if n==True and l<11:
    print(f"Email enter sucssesfuly")
else:
    print("Email= Error")



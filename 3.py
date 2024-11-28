# Practical Example 7: Write a Python program to calculate grades based on percentage
a=int(input("enter a first subject marks:="))
b=int(input("enter a second subject marks:="))
c=int(input("enter a third subject marks:="))
d=a+b+c
e=d/3
if a>=33:
    if b>=33:
         if c>=33:
            if d>=33:
             print("your percentage is=",e)

else:
    print("you are fail!..")


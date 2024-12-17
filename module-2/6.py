#Write python program that swap two number with temp variable and without temp variable
print('-------------------with temp veriable-----------------------')
a=int(input("enter a first number="))
b=int(input("enter a second number="))
temp=a
a=b
b=temp
print("num1 a=",a)
print("num2 b=",b)

print('-------------------without temp veriable-----------------------')
a=int(input("enter a first number="))
b=int(input("enter a second number="))

print("num1 a=",b)
print("num2 b=",a)


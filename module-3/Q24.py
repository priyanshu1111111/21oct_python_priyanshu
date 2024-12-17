# Q24. Write a Python program to convert a list to a tuple. 

test=[]

ch=int(input("Enter number of data: "))

for i in range(ch):
    name=input("Enter Your  Name: ")
    test.append(name)

tuple=tuple(test)

print(f'The List is: {test}\n') 

print(f'After convert List into tuple: {tuple}')


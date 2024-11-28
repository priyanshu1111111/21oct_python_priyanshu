#Write a Python program to create a dictionary of 6 key-value pairs. 

# id={'key':'value'} main thigs to follow...

id={}
n=int(input("enter a value of get keys and values:=="))
for i in range(n):
    x=input("enter a key value==")
    y=input("enter a value==")
    id[x]=y
print(id)


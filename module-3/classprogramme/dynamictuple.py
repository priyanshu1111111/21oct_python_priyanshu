mylist=[]

n=int(input("how many data store you want to="))

for i in range(n):
    x=input("enter element=")
    mylist.append(x)

print(tuple(mylist))
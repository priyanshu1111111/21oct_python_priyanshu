print("welcome")
fl=open('temp.txt','r')
x=int(input("how many student data you shuld store in file??"))
for i in range(x):
    id=input("enter your id")
    name=input("enter your name")
    city=input("enter your city")

    fl.read(f"Id:{id}\nname:{name}\ncity:{city}\n")
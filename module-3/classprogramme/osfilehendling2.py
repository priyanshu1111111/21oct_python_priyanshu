import os

#os.mkdir("stdata")
os.chdir("stdata")
#open("stdata.txt",'x')
x=open('stdata.txt','a')

n=int(input("How many student data you want to store:"))

for i in range(n):
    id=input("Enter ID:")
    nm=input("Enter Name:")
    ct=input("Enter City:")
    x.write(f"\nID={id}\nName={nm}\nCity={ct}\n")
    print("-----------------------------------------")
import os 

#os.mkdir('Table')
os.chdir('Table')
#open('table.txt','x')
x=open('table.txt','a')

n=int(input("How many table you want to print:"))

for i in range(n):
    tab=int(input(f"Enter {i+1} table you want to print:"))
    for j in range(1,11):
        print(tab,'*',j,'=',tab*j)
        x.write(f'{tab}*{j}={tab*j}\n') 
        print("--------------------------------------")
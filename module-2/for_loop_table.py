i=1
j=0
n=int(input("How many table you want to print="))
for i in range(0,n):
    t=int(input("which table you want to print="))
    for j in range(1,11,1):
        print(f"{t} * {j} = {t*j}")
    
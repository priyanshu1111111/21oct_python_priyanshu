fl=open('newfile.txt','a')
x=int(input("how many table you want to print=="))
for i in range(x):
    b=int(input("what number you want to print as a table=="))
    for a in range(1,11):
        n=b*a
        fl.write(f"{b}*{a}=={n}\n")
        
  
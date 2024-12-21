#log generator
import datetime
import random

fl=open('xfile.txt','a')
x=int(input("how many userdata have you input?=="))
for i in range(x):
    created=datetime.datetime.now()
    id=random.randint(1111,9999)
    nm=input("enter a name:==")
    cty=input("enter a city:==")
    fl.write(f"{created}\n {id}\n {nm}\n {cty}\n")

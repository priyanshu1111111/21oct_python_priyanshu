dic={"id":"","name":"","std":"","pass":" "}

# dic["id"]=int(input("enter your id="))
# dic["name"]=input("enter your name=")
# dic["std"]=input("enter your std=")
# dic["pass"]=int(input("enter your password="))

for i in dic.keys():
    dic[i]=input(f"Enter your {i}=")



print(dic)
print("welcome manager")
n=int(input("how many custmer do you have add??"))
for i in range(n):
    nm=input("enter youir name==")
    acn=int(input("enter your account number=="))
    am=int(input(" enter your amount yu should deposit.."))
    if am<=2000:
        print("you are atleast deposit 2more than 2000/-")
    else:
        print("thank you for deposit==",am)
        

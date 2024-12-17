fruitshop={}
print("welocme to fruit shop..")
def addstock():
    v=int(input("how many fruits do you add?.."))
    for i in range(v):

        fname=input("enter a fruit name..==") 
        fqty=(int(input("enter a quantity..== ")))
        fprice=int(input("enter a price of fruits=="))
        fruitshop[fname]={'quantity':fqty,'fruit price':fprice}


def updatestock():
    fname=input("enter a fruit name==")
    fqty=int(input("enter a fruit quantity=="))
    fprice=int(input("enter a fruit price=="))
    if fname in fruitshop.keys():
        fruitshop[fname] = {'Qty':fqty, 'Price':fprice}
    else:
        fruitshop[fname] = {'Qty':fqty, 'Price':fprice}
def viewstock():
    print(fruitshop)
def ftshop():
    print("1..addstock") 
    print("2..viewstock")
    print("3..updatestock")

while True:
    n=int(input("1.manager..""2.customer=="))
    if n==1: 
        print("welcome manager")
        x=ftshop()
        while True:
            
            x=int(input("enter a choice 1 to 4=="))
            if x==1:
                addstock()
            elif x==2:
                viewstock()
            elif x==3:
                updatestock()   
            elif x==4:
                break

        
    if n==2:
        def customer():
            f=int(input("want to buy some ?..press 1 to buy.. and press 2 to show fruits.."))
            if f==1:
                h=input("enter a fruit name")
                h==ftshop
                viewstock()

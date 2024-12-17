# Q29. Write a Python program to unzip a list of tuples into individual lists. 

tuple_list=[(1,2,4,3),('kishan','toliya','rajkot','guj'),(10.3,4,5,6,7,8)]

count=1

for i in tuple_list:
    print(f'List {count}: {list(i)}')
    count+=1



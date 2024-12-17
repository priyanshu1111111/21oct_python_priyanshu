# Q28. Write a Python program to remove an empty tuple(s) from a list of tuples. 

tuple_list=[(1,2,4,3),('kishan','toliya','rajkot','guj'),(10.3,4,5,6,7,8),()]

print(f'Origional List of Tuple: {tuple_list}\n')
for i in tuple_list:
    if len(i) == 0:
        tuple_list.remove(i)

print(f'Removin Empty tuple from tuple_list: {tuple_list}')
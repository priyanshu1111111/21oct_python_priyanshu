# Q31. How will you create a dictionary using tuples in python?

tuple_1=(101,102,103,104,105)

tuple_2=('kishan','jay','parth','zala','yagnik')

total=len(tuple_1)

dict_list={}

for i in range(total):
        dict_list[tuple_1[i]] = tuple_2[i]

print(dict_list)

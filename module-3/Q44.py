# Q44. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. 
# Sample data: {'1': ['a','b'], '2': ['c','d']} 
# Expected Output: 
# ac ad bc bd

d1= {'1': ['a','b'], '2': ['c','d']}

print(f'Dict: {d1}\n')
print('Expected Output:')

d2=[]

for i in d1.values():
    d2.append(i)

lenth=len(d2)

for j in range(lenth):
    for k in range(lenth):
        x=d2[0][j]+d2[1][k]
        print(x,end=" ")



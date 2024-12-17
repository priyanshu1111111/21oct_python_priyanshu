# Q11. Write a Python program to write a list to a file.

list=['Python', 'Coading', 12.5, 'hello', 23, 'Rajkot125']

file=open('file_name.txt','a')

for i in list:
    file.write(f'{str(i)}\n')

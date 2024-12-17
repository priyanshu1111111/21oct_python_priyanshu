# Q4. Write a Python program to read first n lines of a file.


file=open('file_name.txt','a')

file=open('file_name.txt','r')

n=int(input('How many lines You want to read?: '))

for i in range(n):
    print(file.readline())


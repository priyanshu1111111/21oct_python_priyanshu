# Q12. Write a Python program to copy the contents of a file to another file.

file_1=open('file_name.txt','r')

file_2=open('file_2.txt','a')

for i in file_1:
    file_2.write(i)


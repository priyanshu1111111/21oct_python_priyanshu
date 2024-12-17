# Q10. Write a Python program to count the number of lines in a text file.
file=open('file_name.txt','a')

file=open('file_name.txt','r')

count_line=len(file.readlines())

print(count_line)
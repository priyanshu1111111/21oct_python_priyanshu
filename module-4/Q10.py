# Q10. Write a Python program to count the frequency of words in a file.

file=open('file_name.txt','a')

file=open('file_name.txt','r')

data=file.read()

ch=input('Wihich Charecter Frequency Want to Find?: ')

count=0

for i in data:
    if i == ch:
        count+=len(i)

print(count)

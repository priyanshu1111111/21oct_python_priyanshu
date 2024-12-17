# Q3. Write a Python program to append text to a file and display the text.

file=open('file_name.txt','a')

file.write('\nNew Data')

read_data=open('file_name.txt','r')

print(read_data.read())
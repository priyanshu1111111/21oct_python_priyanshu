#11.  Write a python program to sum of the first n positive integers.

n=int(input("Input an integer Number: "))
a=0
for i in range(n):
    i+=1
    a=a+i

print(f"Sum Of the first {n} Positive Integers: {a}")
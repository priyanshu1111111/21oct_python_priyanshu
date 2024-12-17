 #10. Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

a=int(input("Enter Value of a: "))
b=int(input("Enter Value of b: "))

if a == b or a+b == 5 or a-b == 5:
    print("TRUE")
else:
    print("FALSE")
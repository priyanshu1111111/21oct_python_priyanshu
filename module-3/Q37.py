# Q37. Write a Python script to print a dictionary where the keys are numbers between 1 and 15.

dict_1={}

for i in range(16):
    dict_1[f'key_{i+1}'] = f'value_{i+1}' 
    i+=1
    
print(dict_1)

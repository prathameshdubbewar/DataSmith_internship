import numpy as np

def sum_of (num_arr):
    sum = 0
    for i in num_arr:
        sum += i 
    return sum

def product_of(num_arr):
    product = 1
    for i in num_arr:
        product *= i
    return product


lst = input("enter list of numbers: ").split()
num_arr = np.array([int(i) for i in lst])
print(num_arr)

sum_of_ele = sum_of(num_arr)
product_of_ele = product_of(num_arr)

print("sum of elements is : ",sum_of_ele)
print("product of elements is: ",product_of_ele)

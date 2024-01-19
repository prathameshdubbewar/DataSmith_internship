import numpy as np

def calc_dot_product(arr):
    dot_product_result = np.dot(arr, arr)

    return dot_product_result

def dot_product_fun(arr):
    result = sum(i*j for i , j in zip(arr,arr))
    result = sum(arr[i] * arr[i] for i in range(len(arr)))

    return result



arr_input = input("Enter elements of list: ").split()
arr = np.array([int(i) for i in arr_input])

dot_product = calc_dot_product(arr)

print("Dot product of the array is:", dot_product)

dot_prod = dot_product_fun(arr)
print("dot product without using np is: ",dot_prod)

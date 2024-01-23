import numpy as np


def negative_replace(arr):
    for i in range(len(arr)):
        if arr[i]<0:
            arr[i] = 0
    return arr


inpt_arr = input("enter elements of array: ").split()

arr = np.array([int(i) for i in inpt_arr])

print("initial array is:{} ".format(arr))
output_arr = negative_replace(arr)

print("array without negative values is:{} ".format(output_arr))
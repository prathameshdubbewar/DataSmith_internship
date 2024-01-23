import numpy as np

def dot_product(arr1, arr2):
    if len(arr1) != len(arr2):
        return "arrays must have the same length."
    
    result = sum(x * y for x, y in zip(arr1, arr2))
    return result

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

result_product = dot_product(array1, array2)

print("Dot product of arrays:")
print(result_product)

import numpy as np

def horizontal_concatenate(arr1, arr2):

    concatenated_array = np.concatenate((arr1, arr2))
    return concatenated_array

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

result_concatenation = horizontal_concatenate(array1, array2)

print("Concatenated Array:")
print(result_concatenation)

import numpy as np

def matrix_input():
    rows = int(input("Enter the number of rows: "))
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter elements for row {i + 1}: ").split()))
        matrix.append(row)
    return np.array(matrix)



array_1d = input("Enter the elements of the 1D array :").split()
array_is = np.array([int(i) for i in array_1d ])

array_2d = matrix_input()

result_array = array_2d + array_1d

print("Resultant array")
print(result_array)

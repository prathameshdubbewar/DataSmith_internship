import numpy as np
def matrix_input():
    rows = int(input("Enter the number of rows: "))
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter elements for row {i + 1}: ").split()))
        matrix.append(row)
    return np.array(matrix)

array_2d = matrix_input()

row_sums = np.sum(array_2d, axis=1)

normalized_array = array_2d / row_sums

print("original array:")
print(array_2d)
print("normalized  Array:")
print(normalized_array)

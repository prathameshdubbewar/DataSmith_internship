import numpy as np

def matrix_input(rows):
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter elements for row {i + 1}: ").split()))
        matrix.append(row)
    return np.array(matrix)


rows_a = int(input("Enter number of rows in matrix A: "))
array1 = matrix_input(rows_a)

rows_b = int(input("Enter rows in matrix B: "))
array2 = matrix_input(rows_b)

vertical_stack = np.vstack((array1, array2))

horizontal_stack = np.hstack((array1, array2))

split_vertical = np.vsplit(vertical_stack, 2)

split_horizontal = np.hsplit(horizontal_stack, [3])

print("Array 1:")
print(array1)

print("Array 2:")
print(array2)

print("Vertical Stacked:")
print(vertical_stack)

print("HoriStacked:")
print(horizontal_stack)

print("Split Vertically Stacked Array:")
print(split_vertical)

print("Split Horizontally Stacked Array:")
print(split_horizontal)



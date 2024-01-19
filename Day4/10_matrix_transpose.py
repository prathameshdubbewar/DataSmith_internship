import numpy as np

def transpose_matrix(arr):
    transposed = np.transpose(arr)
    return transposed 

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transposed = [[matrix[j][i] for j in range(rows)] for i in range(cols)]

    return transposed

def matrix_creation(mat_row):
    matrix=[]
    for i in range (mat_row):
        row = input(f"Enter elements for row {i + 1} : ").split()
        lst = [int(i) for i in row]
        
        matrix.append(lst)
    return matrix 


mat_row = int(input("enter number of rows of a martrix:"))
matrix = matrix_creation(mat_row)

transpose_output = transpose_matrix(matrix)

print("Original Array:")
for i in matrix:
        print(i)
print("Transposed Array:")
print(transpose_output)
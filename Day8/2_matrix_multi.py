import numpy as np

def matrix_input(rows):
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter elements for row {i + 1}: ").split()))
        matrix.append(row)
    return np.array(matrix)


def matrix_multiply(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print("No multiplication  possible.")
        

    result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

rows_a = int(input("Enter number of rows in matrix A: "))
matrix_a = matrix_input(rows_a)

rows_b = int(input("Enter rows in matrix B: "))
matrix_b = matrix_input(rows_b)

result_matrix = matrix_multiply(matrix_a, matrix_b)
print("Result: ")
for row in result_matrix:
        print(row)
def get_matrix_from_user(rows, cols):
    matrix = []
    print(f"Enter the elements for a {rows}x{cols} matrix:")
    
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Enter element at position ({i + 1}, {j + 1}): "))
            row.append(element)
        matrix.append(row)
    
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

def matrix_multiply(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print("Matrix multiplication not possible.")
        return None

    result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result


rows_a = int(input("Enter  number of rows in matrix A: "))
cols_a = int(input("Enter  number of columns in matrix A: "))
matrix_a = get_matrix_from_user(rows_a, cols_a)

rows_b = int(input("Enter number of rows in matrix B: "))
cols_b = int(input("Enter number of columns in matrix B: "))
matrix_b = get_matrix_from_user(rows_b, cols_b)

result_matrix = matrix_multiply(matrix_a, matrix_b)
print("Result: ")
print_matrix(result_matrix)

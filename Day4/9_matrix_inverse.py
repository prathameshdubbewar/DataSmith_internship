import numpy as np

def inverse_matrix(matrix):
        det = np.linalg.det(matrix)
        if det != 0:
            inverse_matrix = np.linalg.inv(matrix)
            return inverse_matrix
        
        # logic without numpy only for 2x2 matrix
def inverse_matrix_2by2(matrix):
    if matrix.shape == (2, 2):
        det = matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]
        if det != 0:
            inv_det = 1 / det
            inverse_matrix = np.array([[matrix[1, 1], -matrix[0, 1]], [-matrix[1, 0], matrix[0, 0]]])
            inverse_matrix *= inv_det
            return inverse_matrix
        
def matrix_creation(mat_row):
    matrix=[]
    for i in range (mat_row):
        row = input(f"Enter elements for row {i + 1} : ").split()
        lst = [int(i) for i in row]

#       row = list(map(int, input(f"Enter elements for row {i + 1} : ").split()))
        
        matrix.append(lst)
    return matrix 


mat_row = int(input("enter number of rows of a martrix:"))
matrix = matrix_creation(mat_row)

inverse_result = inverse_matrix(matrix)

print("Initial Matrix:")
print(matrix)
print("Inverse Matrix:")
print(inverse_result)

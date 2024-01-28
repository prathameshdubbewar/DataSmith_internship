import numpy as np

def matrix_input():
    rows = int(input("Enter the number of rows: "))
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter elements for row {i + 1}: ").split()))
        matrix.append(row)
    return np.array(matrix)

matrix = matrix_input()

eigenvalues, eigenvectors = np.linalg.eig(matrix)

print("Eigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)

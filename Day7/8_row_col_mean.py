import numpy as np


def sum_row_column(arr):
    np_array = np.array(arr)
    row_sum = np.mean(np_array, axis=1)
    col_sum = np.mean(np_array, axis=0)
    return row_sum, col_sum

num_rows = int(input("Enter the number of rows: "))

list_of_lists = []
for i in range(num_rows):
    row = list(map(int, input(f"Enter elements for row {i + 1} : ").split()))
    list_of_lists.append(row)

row_sum, col_sum = sum_row_column(list_of_lists)

print("initial array: ")
print(np.array(list_of_lists))
print("mean of elements in each row:")
print(row_sum)
print("mean of elements in each column:")
print(col_sum)

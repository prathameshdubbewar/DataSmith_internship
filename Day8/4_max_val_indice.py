import numpy as np

rows = int(input("enter number of rows"))
cols = int(input("enter number of cols"))

random_array = np.random.randint(0,100, size=(rows,cols))

max_val = np.max(random_array)

max_value = float('-inf')
max_row, max_col = -1, -1

for i in range(len(random_array)):
    for j in range(len(random_array[0])):
        if random_array[i][j] > max_value:
            max_value = random_array[i][j]
            max_row, max_col = i, j

print("Maximum Value:", max_value)
print("Indices of Maximum Value:", (max_row, max_col))
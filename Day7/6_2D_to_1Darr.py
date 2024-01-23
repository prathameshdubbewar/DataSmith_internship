import numpy as np 
def flatten_arr(row,cols):

    rand_arr = np.random.randint(0,10, size =(row,cols))

    flatt_arr = rand_arr.flatten()
    return rand_arr,flatt_arr

num_row = int(input("enter number of rows: "))
num_cols = int(input("enter number of cols: "))

rand_arr , flatt_arr = flatten_arr(num_row,num_cols)

print("initial random 2d array is: ")
print(rand_arr)
print("flattened 1d array is:")
print(flatt_arr)

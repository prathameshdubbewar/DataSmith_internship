import numpy as np

lst = input("enter list of numbers: ").split()
data_arr = np.array([int(i) for i in lst])

sorted =np.sort(data_arr)

print("sorted array is : ",sorted) 
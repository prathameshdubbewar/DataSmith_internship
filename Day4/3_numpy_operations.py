import numpy as np


lst = input("enter list of numbers: ").split()
data_arr = np.array([int(i) for i in lst])


mean_value = np.mean(data_arr)
median_value = np.median(data_arr)
std_deviation = np.std(data_arr)

print("array_elements:", data_arr)
print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_deviation)

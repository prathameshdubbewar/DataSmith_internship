import numpy as np

def normalize_array(arr):
    mean = np.mean(arr)
    std_dev = np.std(arr)

    normalized_arr = (arr - mean) / std_dev

    return normalized_arr

input_array = np.array([1, 2, 3, 4, 5])
normalized_array = normalize_array(input_array)

print("Initial array:", input_array)
print("Normalized array:", normalized_array)

import numpy as np

def mse(predicted_values, actual_values):
    if len(predicted_values) != len(actual_values):
        return "invalid input"
    mse = np.mean((predicted_values - actual_values) ** 2)
    return mse

predicted_values = np.array([1, 2, 3, 4, 5])
actual_values = np.array([2, 3, 4, 5, 6])

mse_result = mse(predicted_values, actual_values)

print("MSE of the values is :", mse_result)

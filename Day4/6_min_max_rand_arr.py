import numpy as np

random_ints = np.random.randint(1,101, size=10)


print("Random Array:")
print(random_ints)

max_value = np.max(random_ints)
min_value = np.min(random_ints)


print("Maximum Value:", max_value)
print("Minimum Value:", min_value)

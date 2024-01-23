import numpy as np

gap_size = 0.5
sequence = []

for value in np.arange(0, 10 + gap_size, gap_size):
    sequence.append(value)

sequence = np.array(sequence)

print("New Sequence:")
print(sequence)

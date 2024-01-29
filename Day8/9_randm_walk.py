# REVISE AGAIN

import numpy as np
import matplotlib.pyplot as plt

num_steps = 100

steps = np.random.choice([-1, 1], size=num_steps)

position = np.cumsum(steps)

plt.plot(position)
plt.xlabel('time step')
plt.ylabel('position')
plt.show()

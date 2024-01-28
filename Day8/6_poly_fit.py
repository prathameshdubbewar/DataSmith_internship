import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
x = np.linspace(0, 10, 20)
y_true = np.sin(x) + np.random.normal(0, 0.5, x.size)

degree = 3
coefficients = np.polyfit(x, y_true, degree)
poly = np.poly1d(coefficients)

y_fit = poly(x)

plt.figure(figsize=(8, 6))
plt.scatter(x, y_true, label='Noisy Data', color='blue')
plt.plot(x, y_fit, label='Fitted Polynomial', color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Polynomial Fitting')
plt.legend()
plt.grid(True)
plt.show()

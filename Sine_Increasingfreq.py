# Calculate the sine wave with increasing frequency
import numpy as np
import matplotlib.pyplot as plt

frequency = 0.005
t = np.arange(0.0, 10.0, 0.01)

for i in range(1,10):
    frequency = frequency + 0.1
    y = np.sin(2 * np.pi * frequency * t)
    plt.plot(t, y)

plt.show()

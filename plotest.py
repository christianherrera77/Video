import numpy as np
import matplotlib.pyplot as plt

# First create some toy data:
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)

# Create just a figure and only one subplot
fig, ax = plt.subplots(2,2)
ax[0, 0].plot(x, y)
ax[0, 0].set_title('Simple plot')
plt.show()
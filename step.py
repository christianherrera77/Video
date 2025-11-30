import matplotlib.pyplot as plt
import numpy as np

num_points = 44100
amplitude = 1
frequency = 1
t = np.arange(num_points)
#y = np.sin(t / 2)
y = amplitude*np.sin(2 * np.pi * frequency * t)

plt.step(t, y, where='post', label='post')
plt.plot(t, y, 'o--', color='grey', alpha=0.3)

plt.grid(axis='x', color='0.95')
plt.legend(title='Parameter where:')
plt.title('plt.step(where=...)')
plt.show()
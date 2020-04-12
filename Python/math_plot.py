import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

M = np.random.rand(10, 10, 10)

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

counter = range(10)

x, y, z = np.meshgrid(counter, counter, counter)

ax.scatter(x, y, z, c=M.flat)

plt.show()

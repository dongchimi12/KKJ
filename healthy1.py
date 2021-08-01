import numpy as np
import matplotlib.pyplot as plt

rs = np.random.RandomState(10)
x = 10 * rs.rand(100)
y = 3 * x + 2 * rs.rand(100)

plt.scatter(x, y, s=10);
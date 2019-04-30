import numpy as np
import matplotlib.pyplot as plt

N = 10000
X = 2*np.random.random((N, 2)) - 1
Y = np.zeros(N)
Y[(X[:,0] > 0) & (X[:,1] < 0)] = 1
Y[(X[:,0] < 0) & (X[:, 1] > 0)] = 1

plt.scatter(X[:, 0], X[:, 1], c=Y)
plt.show()





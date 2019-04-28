# Goal is to visually "demonstrate" Central Limit Theorem 
# Recall Central Limit Theorem
# If Y = X1 + X2 + X3 + ... + Xn
# Where the Xs are random variables from any distribution
# Then as N ---> Infinity, Y ---> Guassian Distribution
import numpy as np
import matplotlib.pyplot as plt
print("Computing ... Wait till done")
Y = []
for i in range(10000):
    M = np.random.random(10000).sum()
    Y.append(M)
plt.hist(Y, bins=20)
plt.show()
print("Done Computing :)")
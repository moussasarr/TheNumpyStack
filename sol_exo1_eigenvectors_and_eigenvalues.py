import numpy as np
import matplotlib.pyplot as plt

#Initial arrays
A = np.array([ [0.3, 0.6, 0.1], [0.5, 0.2, 0.3], [0.4, 0.1, 0.5] ])
V = np.array([ 1.0/2.0, 1.0/2.0, 1.0/2.0])
Vprime = np.array([])

#Euclidan distance between Vprime and V
Veucl = []
i = 0
for i in range(25):
	Vprime  = V.dot(A)
	Veucl.append(np.linalg.norm(Vprime - V))
	V = Vprime


#Plotting euclidean distance |V' - V| as a function of each iteration
plt.plot(Veucl)
plt.show()

# Plotting |V' - V| 
# We realize that |V' -V| tends to 0
# Meaning that V' = V = AV
# So V = AV
# This infers that V is an eigenVector of A for the corresponding 
# eigenValue of 1
# Meaning the vector V transforms unit vector of A unchanged.

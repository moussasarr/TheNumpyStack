# Load data 2d using python
# Convert it into a numpy array
# Using Manual Loading 
DATA = []
for line in open('data_2d.csv'):
    row = line.split(',')
    sample = map(float, row)
    DATA.append(sample)
    #print(sample)

# Data is now a list of lists, so we can convert it into a numpy array
import numpy as np
A = np.array(DATA)
print(A)
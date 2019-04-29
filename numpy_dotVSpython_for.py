import numpy as np 
from datetime import datetime

a = np.random.randn(100)
b = np.random.randn(100)
T = 100000

def slow_product(a, b):
	dot = 0;
	for x,y in zip(a,b):
		dot += x*y
		return dot


t0 = datetime.now()

for t in range(T):
	slow_product(a, b)
dt1 = datetime.now() - t0


t0 = datetime.now()
for t in range(T):
 t2 = a.dot(b)
dt2 = datetime.now() - t0

print "dt1/dt2 = ", dt1.total_seconds() / dt2.total_seconds()
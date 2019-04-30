# A function that test whether or not a matrix is symmetric
# The Implicit Way (using numpy functions)
# Also using the manual way
import numpy as np

def is_symmetric1(matrix):
	# Assuming input matrix is a numpy array
	symmetry = True
	I, J = matrix.shape
	# A symmetric matrix is a square matrix
	if I != J:
		return False
	# A symmetric matrix transpose is itself
	for i in range(I):
		for j in range(J):
			if matrix[i, j] != matrix[j, i]:
				return False
	return symmetry

def is_symmetric2(matrix):
	# Assuming input matrix is a numpy array
	transpose = matrix.transpose()
	if np.array_equal(matrix, transpose):
		return True
	return False

#Testing our functions
Sym1 = np.zeros((10, 10))
Sym2 = np.ones((5, 5))
Asym1 = np.zeros((10,4))
Asym2 = np.ones((3, 6))

print("Sym1 is symmetric: ")
print(is_symmetric1(Sym1))
print("Sym1 is symmetric :")
print(is_symmetric2(Sym1))
print("Sym2 is symmetric: ")
print(is_symmetric1(Sym2))
print("Sym2 is symmetric: ")
print(is_symmetric2(Sym2))


print("Asym1 is symmetric: ")
print(is_symmetric1(Asym1))
print("Asym2 is symmetric: ")
print(is_symmetric2(Asym2))
print("Asym1 is symmetric:")
print(is_symmetric2(Asym1))
print("Asym2 is symmetric")
print(is_symmetric1(Asym2))
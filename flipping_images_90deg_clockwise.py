import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt


def get_2by2_Rotation_matrix(alpha):
	R = np.array([[ np.cos(np.deg2rad(alpha)), -np.sin(np.deg2rad(alpha))], 
		          [ np.sin(np.deg2rad(alpha)), np.cos(np.deg2rad(alpha))]])
	return R

def NpFlip90Clockwise(image):
	return np.rot90(image, 3)

def ManuallyFlip90Clockwise(image):
	H, W = image.shape
	res = np.zeros((W, H))

	for i in range(H):
		for j in range(W):
			res[i, j] = image[W-j-1, i]
	return res

def ManuallyFlip90AntiClockwise(image):
	H, W = image.shape
	res = np.zeros((W, H))

	for i in range(H):
		for j in range(W):
			res[i, j] = image[j, H-i-1]
	return res	

#def Flip45degClockwise(image):
#	H, W = image.shape
#	R = getRotation_matrix(-45)
#	res = np.zeros((W, H))

#	for i in range(H):
#		for j in range(W):
#			res[i, j] = R.dot(image[i, j])
#	return res

#def Flip45degAntiClockwise(image):
#	H, W = image.shape
#	R = getRotation_matrix(45)
#	res = np.zeros((W, H))

#	for i in range(H):
#		for j in range(W):
#			res[i, j] = R.dot([[image[i]], [image[j]]])
#	return res



#Flip General Image Data for an arbitrary image at an arbitrary angle 
#def flipImagePixels(image, angle):


mnist_set = pd.read_csv("train.csv")
data = mnist_set.values

images = data[:, 1:]
labels = data[:, 0]

for i in range(10):
	IMi = images[labels == i]
	Mean = IMi.mean(axis=0)
	im = Mean.reshape(28, 28)
	im = NpFlip90Clockwise(im)

	plt.imshow(im, cmap='gray')
	plt.show()


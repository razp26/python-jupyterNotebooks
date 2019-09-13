import cv2 as cv 
import sklearn
from sklearn.cluster import KMeans

# Reading image
img = cv.imread('frutas.jpg')

# Reshaping image to a list of pixels
img = img.reshape((img.shape[0] * img.shape[1], 3))

# Using k-means with our list of pixels
clusters = KMeans(n_clusters = 6)
clusters.fit(img)

# print(clusters.labels_)


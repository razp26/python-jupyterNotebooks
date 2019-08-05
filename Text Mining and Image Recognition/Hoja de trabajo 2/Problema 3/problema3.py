import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def img3dGray(imgName, x, y):
    img = cv2.imread(imgName, 0)
    alto = img.shape[0]
    ancho = img.shape[1]

    x_ancho, y_alto = np.mgrid[0:alto, 0:ancho]
    pltImg = plt.figure(figsize=(5,5))

    projection = pltImg.gca(projection="3d")
    projection.plot_surface(x_ancho, y_alto, img, rstride=1, cstride=1, cmap=plt.cm.gray, linewidth=1)
    projection.view_init(x,y)
    plt.show()

img3dGray("test_image.jpg", 45,45)
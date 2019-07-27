import cv2
import numpy as np
import sys

def divideColorImage(imgColorFile):
    # Leemos las imagenes recibidas como parametros
    imgColor = cv2.imread(imgColorFile)

    alto = imgColor.shape[0]
    ancho = imgColor.shape[1]
    canales = imgColor.shape[2]

    # Creamos una matriz de pixeles inicializada a cero que se utilizara para unificar la imagen
    imgSalidaVerde = np.zeros((alto, ancho, 1))
    imgSalidaRojo = np.zeros((alto, ancho, 1))
    imgSalidaAzul = np.zeros((alto, ancho, 1))

    # Recorremos las imagenes pixel por pixel
    for i in range(alto):
        for j in range(ancho):
            pixel = imgColor[i,j]
            imgSalidaAzul[i,j] = pixel[0]
            imgSalidaVerde[i,j] = pixel[1]
            imgSalidaRojo[i,j] = pixel[2]

    # Guardamos la imagen
    cv2.imwrite("image_gris_azul.jpg", imgSalidaAzul)
    cv2.imwrite("image_gris_verde.jpg", imgSalidaVerde)
    cv2.imwrite("image_gris_rojo.jpg", imgSalidaRojo)


divideColorImage('test_image.JPG')
sys.exit()
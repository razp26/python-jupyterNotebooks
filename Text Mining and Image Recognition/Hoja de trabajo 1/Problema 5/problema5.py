import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt

def imgToWeightedGray(imgColorFile):
    # Leemos las imagenes recibidas como parametros
    imgColor = cv2.imread(imgColorFile)

    alto = imgColor.shape[0]
    ancho = imgColor.shape[1]
    canales = imgColor.shape[2]

    pesoRojo = 0.3
    pesoVerde = 0.59
    pesoAzul = 0.11

    # Creamos una matriz de pixeles inicializada a cero que se utilizara para unificar la imagen
    imgGris = np.zeros((alto, ancho, 1))

    # Recorremos las imagenes pixel por pixel
    for i in range(alto):
        for j in range(ancho):
            pixel = imgColor[i,j]
            imgGris[i,j] = (pesoAzul * pixel[0]) + pesoVerde * pixel[1] + pesoRojo * pixel[2]

    # Guardamos la imagen
    cv2.imwrite("img_gris_ponderado.jpg", imgGris)

    # Mostramos la imagen recien guardada
    newImg = cv2.imread("img_gris_ponderado.jpg")
    cv2.imshow('Imagen en escala de grises ponderados', newImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

imgToWeightedGray("test_image.JPG")
sys.exit()

import cv2
import numpy as np
import sys


def main():
    imgStr = "20180309_090603.jpg"
    img = cv2.imread(imgStr)
    cv2.imshow('Imagen', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Obtenemos las dimensiones de la imagen, así como los canales (RGB)
    alto = img.shape[0]
    ancho = img.shape[1]
    canales = img.shape[2]

    # Creamos una matriz de pixeles inicializada a cero
    gris = np.zeros((alto, ancho, 1))

    # Recorremos la imagen para convertirla a escala de grises
    for i in range(alto):
        for j in range(ancho):
            pixel = img[i,j]
            grisAritmetico = int(pixel[0]) + int(pixel[1]) + int(pixel[2])/3
            gris[i,j] = grisAritmetico

    # Guardamos la imagen en escala de grises
    cv2.imwrite('grises_' + imgStr, gris)

    # Mostramos la imagen recién guardada
    img_gris = cv2.imread('grises_' + imgStr)
    cv2.imshow('Imagen grises', img_gris)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    sys.exit()

main()

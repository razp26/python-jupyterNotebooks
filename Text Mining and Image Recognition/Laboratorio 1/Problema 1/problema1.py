import cv2
import numpy as np
import sys

def imgEQ(imgName):
    # Leemos la imagen recibida como parametro
    img = cv2.imread(imgName, 0)

    # Obtenemos las dimensiones de la imagen, asi como los canales (RGB)
    alto = img.shape[0]
    ancho = img.shape[1]
    imgSalida = np.zeros((alto,ancho))

    histograma = np.zeros((256))
    intensidad = range(0,256)

    # Recorremos la imagen pixel por pixel
    for i in range(alto):
        for j in range(ancho):
            pixel = img[i,j]
            histograma[pixel]+=1 
    
    suma = np.sum(histograma)
    histograma = histograma/suma
    cdf = getCDF(histograma)

    # Recorremos la imagen pixel por pixel
    for i in range(alto):
        for j in range(ancho):
            pixel = img[i,j]
            imgSalida[i,j] = 255 * cdf[pixel]

    # Guardamos la imagen
    cv2.imwrite("eq_" + imgName, imgSalida)


def getCDF(hist):
    cumm = np.zeros((256))
    sum = 0

    for i in range(len(hist)):
        sum = sum + hist[i]
        cumm[i] = sum

    return cumm


imgStr = "test_image.jpg"
imgEQ(imgStr)

imgStr = "drums.jpg"
imgEQ(imgStr)

sys.exit()


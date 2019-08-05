import cv2
import numpy as np
import sys

def imgBinarization(imgName, umbral):
    # Leemos la imagen recibida en el parametro imgName
    inImg = cv2.imread(imgName)

    # Leemos las propiedades de la imagen
    alto = inImg.shape[0]
    ancho = inImg.shape[1]
    canales = inImg.shape[2]

    # Creamos un arreglo de pixeles para la imagen de salida, esta tendrá únicamente 1 canal
    outImg = np.zeros((alto,ancho))


    # Recorremos la imagen pixel a pixel
    for i in range(alto):
        for j in range(ancho):
            # Leemos el pixel en la posicion i,j
            pixel = inImg[i,j]
            suma_canales = 0
            total_umbral = umbral * canales
            for c in range(canales-1):
                suma_canales = suma_canales + pixel[c]
            
            if suma_canales > total_umbral:
                outImg[i,j] = 255
            else:
                outImg[i,j] = 0
        
    # Procedemos a guardar la imagen
    outImgName = "binary_img_" + str(canales) + ".jpg"
    cv2.imwrite(outImgName, outImg)

    # Mostramos la imagen recien guardada
    newImg = cv2.imread(outImgName)
    cv2.imshow('Imagen binarizada', newImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


imgBinarization("test_image.JPG", 90)
sys.exit(0)
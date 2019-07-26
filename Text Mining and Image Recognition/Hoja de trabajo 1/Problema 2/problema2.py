import cv2
import numpy as np
import sys

def unifyImgColor(imgFileNameBlue, imgFileNameGreen, imgFileNameRed, imgColorFile):
    # Leemos las imágenes recibidas como parámetros
    imgBlue = cv2.imread(imgFileNameBlue)
    imgGreen = cv2.imread(imgFileNameGreen)
    imgRed = cv2.imread(imgFileNameRed)

    if imgBlue.shape == imgGreen.shape and imgBlue.shape == imgRed.shape:
        # Obtenemos las dimensiones de las imágenes
        alto = imgBlue.shape[0]
        ancho = imgBlue.shape[1]
        canales = imgBlue.shape[2]

        # Creamos una matriz de pixeles inicializada a cero que se utilizará para unificar la imágen
        imgSalida = np.zeros((alto, ancho, canales))

        # Recorremos las imagenes pixel por pixel
        for i in range(alto):
            for j in range(ancho):
                redPixel = imgRed[i,j]
                bluePixel = imgBlue[i,j]
                greenPixel = imgGreen[i,j]

                # Escribimos los pixeles de cada imagen en la imagen que contiene los tres colores
                imgSalida[i,j] = [bluePixel[0], greenPixel[1], redPixel[2]]

        # Guardamos la imagen
        cv2.imwrite(imgColorFile, imgSalida)

        # Mostramos la imagen recien guardada
        newImg = cv2.imread(imgColorFile)
        cv2.imshow('Imagen a colores', newImg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


unifyImgColor("imagen1\\imagen1_salida_gray_azul.jpg", "imagen1\\imagen1_salida_gray_verde.jpg", "imagen1\\imagen1_salida_gray_rojo.jpg", "imagen1_salida_colores.jpg")
unifyImgColor("imagen2\\imagen2_salida_gray_azul.jpg", "imagen2\\imagen2_salida_gray_verde.jpg", "imagen2\\imagen2_salida_gray_rojo.jpg", "imagen2_salida_colores.jpg")
unifyImgColor("perro\\perro_salida_gray_azul.jpg", "perro\\perro_salida_gray_verde.jpg", "perro\\perro_salida_gray_rojo.jpg", "perro_salida_colores.jpg")
sys.exit()
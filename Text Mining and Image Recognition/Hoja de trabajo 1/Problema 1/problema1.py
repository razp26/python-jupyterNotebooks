import cv2
import numpy as np
import sys

def imgColorManipulation(imgName, colorOption):
    # Leemos la imagen recibida como parametro
    img = cv2.imread(imgName)

    # Obtenemos las dimensiones de la imagen, asi como los canales (RGB)
    alto = img.shape[0]
    ancho = img.shape[1]
    canales = img.shape[2]

    # Validamos la opcion recibida como parametro
    if colorOption == 1:
        # Se muestra unicamente el color azul activo
        imgCanales = np.array([0])
    elif colorOption == 2:
        # Se muestra unicamente activo el color verde
        imgCanales = np.array([1])
    elif colorOption == 3:
        # Se muestra unicamente activo el color rojo
        imgCanales = np.array([2])
    elif colorOption == 10:
        # Se muestra unicamente activo los colores rojo y verde
        imgCanales = np.array([2,1])
    elif colorOption == 20:
        # Se muestra unicamente activo los colores verde y azul
        imgCanales = np.array([1,0])
    elif colorOption == 30:
        # Se muestra unicamente activo los colores azul y rojo
        imgCanales = np.array([0,2])

    # Creamos una matriz de pixeles inicializada a cero
    imgSalida = np.zeros((alto, ancho, canales))

    # Recorremos la imagen pixel por pixel
    for i in range(alto):
        for j in range(ancho):
            pixel = img[i,j]

            newPixelRojo = 0
            newPixelVerde = 0
            newPixelAzul = 0

            for c in imgCanales:
                if c == 0:
                    # azul
                    newPixelAzul = pixel[c]
                elif c == 1:
                    # verde
                    newPixelVerde = pixel[c]
                elif c == 2:
                    # rojo
                    newPixelRojo = pixel[c]
            
            imgSalida[i,j] = [newPixelAzul, newPixelVerde, newPixelRojo]

    # Guardamos la imagen
    newImgName = str(colorOption) + '_' + imgName
    cv2.imwrite(newImgName, imgSalida)

    # Mostramos la imagen recien guardada
    newImg = cv2.imread(newImgName)
    cv2.imshow('Imagen manipulada', newImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    sys.exit()

imgStr = "test_image.jpg"
imgColorManipulation(imgStr, 30)

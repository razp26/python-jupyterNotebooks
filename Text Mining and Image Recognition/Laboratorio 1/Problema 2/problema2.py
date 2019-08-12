import cv2
import numpy as np 
import math 

def readGrayScaleImg(imgName):
    return cv2.imread(imgName, 0)

def convolucion(img, kernel):
    # Dimensiones de la imagen
    alto = img.shape[0]
    ancho = img.shape[1]

    # Dimensiones del kernel
    k_alto = np.size(kernel,0)
    k_ancho = np.size(kernel,1)

    # Obtenemos el tamaño del paso
    s_alto = int(k_alto/2)
    s_ancho = int(k_ancho/2)

    # Inicializamos la nueva imagen
    newImg = np.zeros((alto, ancho,1))

    # recorremos la imagen
    for i in range(s_alto, alto - s_alto):
        for j in range(s_ancho, ancho - s_ancho):

            suma = 0
            img_kernel_shape = img[i - s_alto:i + s_alto, j - s_ancho: j + s_ancho]
            for i_k in range(0, k_alto -1):
                for j_k in range(0, k_ancho -1):
                    suma = suma + (kernel[i_k,j_k] * img_kernel_shape[i_k,j_k])
            
            # Asignamos el valor del pixel en la nueva imagen ya con el filtro de convolucion
            newImg[i,j] = suma

    return newImg


def canny(imgName):
    # Leemos la imagen de entrada en escala de grises
    img = readGrayScaleImg(imgName)

    # 1 - Etapa de suavizar por medio de convolucion
    kernel = np.array([[1,2,1],[2,4,2], [1,2,1]])
    kernel = (1/16) * kernel
    newImg = convolucion(img, kernel)

    # Recorremos la imagen
    alto = newImg.shape[0]
    ancho = newImg.shape[1]

    # Definimos nuestra matriz de gradientes
    imgGradiente = np.zeros((alto, ancho, 1))

    # Definimos la matriz de fase
    imgFase = np.zeros((alto, ancho, 1))

    for i in range (0,alto):
        for j in range(0,ancho):
            # Calculamos las derivadas dx y dy
            dx = 0
            dy = 0
            if i < alto - 1:                
                dy = newImg[i+1,j] - newImg[i,j]
            if j < ancho - 1:
                dx = newImg[i, j+1] - newImg[i,j]

            # Calculamos la magnitud del gradiente
            g = math.sqrt((dx*dx) + (dy*dy))
            imgGradiente[i,j] = g

            # Calculamos teta
            teta_radianes = math.atan2(abs(dy), abs(dx))
            teta_grados = math.degrees(teta_radianes)
            imgFase[i,j] = teta_grados

    # Aplicamos el algoritmo de NO supresion maxima y threshold a la matriz de gradiente
    # Definimos los valores de threhold alto y threshold bajo
    thresholdAlto = 15
    thresholdBajo = 10

    # Inicializamos la matriz de salida del NSM
    imgNSM = np.zeros((alto, ancho, 1))
    for i in range (1,alto-1):
        for j in range(1,ancho-1):

            # Inicializamos los valores de los vecinos
            vecinoAnterior = 0
            vecinoSiguiente = 0

            if imgFase[i,j] >= 0 and imgFase[i,j] < 22.5:
                # Horizontal
                vecinoAnterior = imgGradiente[i,j-1]
                vecinoSiguiente = imgGradiente[i,j+1]

            if imgFase[i,j] >= 22.5 and imgFase[i,j] < 45:
                # Diagonal
                vecinoAnterior = imgGradiente[i-1,j-1]
                vecinoSiguiente = imgGradiente[i+1,j+1]

            if imgFase[i,j] >= 45 and imgFase[i,j] < 67.5:
                # Diagonal
                vecinoAnterior = imgGradiente[i-1,j-1]
                vecinoSiguiente = imgGradiente[i+1,j+1]

            if imgFase[i,j] >= 67.5 and imgFase[i,j] < 90:
                # Vertical
                vecinoAnterior = imgGradiente[i+1,j]
                vecinoSiguiente = imgGradiente[i-1,j]

            if imgFase[i,j] >= 90 and imgFase[i,j] < 112.5:
                # Vertical
                vecinoAnterior = imgGradiente[i+1,j]
                vecinoSiguiente = imgGradiente[i-1,j]

            if imgFase[i,j] >= 112.5 and imgFase[i,j] < 135:
                # Diagonal
                vecinoAnterior = imgGradiente[i+1,j-1]
                vecinoSiguiente = imgGradiente[i-1,j+1]

            if imgFase[i,j] >= 135 and imgFase[i,j] < 157.5:
                # Diagonal
                vecinoAnterior = imgGradiente[i+1,j-1]
                vecinoSiguiente = imgGradiente[i-1,j+1]

            if imgFase[i,j] >= 157.5 and imgFase[i,j] < 180:
                # Horizontal
                vecinoAnterior = imgGradiente[i,j-1]
                vecinoSiguiente = imgGradiente[i,j+1]

            if imgFase[i,j] >= 180 and imgFase[i,j] < 202.5:
                # Horizontal
                vecinoAnterior = imgGradiente[i,j-1]
                vecinoSiguiente = imgGradiente[i,j+1]

            if imgFase[i,j] >= 202.5 and imgFase[i,j] < 225:
                # Diagonal
                vecinoAnterior = imgGradiente[i-1,j-1]
                vecinoSiguiente = imgGradiente[i+1,j+1]

            if imgFase[i,j] >= 225 and imgFase[i,j] < 247.5:
                # Diagonal
                vecinoAnterior = imgGradiente[i-1,j-1]
                vecinoSiguiente = imgGradiente[i+1,j+1]

            if imgFase[i,j] >= 247.5 and imgFase[i,j] < 270:
                # Vertical
                vecinoAnterior = imgGradiente[i+1,j]
                vecinoSiguiente = imgGradiente[i-1,j]

            if imgFase[i,j] >= 270 and imgFase[i,j] < 292.5:
                # Vertical
                vecinoAnterior = imgGradiente[i+1,j]
                vecinoSiguiente = imgGradiente[i-1,j]

            if imgFase[i,j] >= 292.5 and imgFase[i,j] < 315:
                # Diagonal
                vecinoAnterior = imgGradiente[i+1,j-1]
                vecinoSiguiente = imgGradiente[i-1,j+1]

            if imgFase[i,j] >= 315 and imgFase[i,j] < 337.5:
                # Diagonal
                vecinoAnterior = imgGradiente[i+1,j-1]
                vecinoSiguiente = imgGradiente[i-1,j+1]

            if imgFase[i,j] >= 337.5 and imgFase[i,j] < 360:
                # Horizontal
                vecinoAnterior = imgGradiente[i,j-1]
                vecinoSiguiente = imgGradiente[i,j+1]

            # Comparamos los valores de los vecinos
            if imgGradiente[i,j] < vecinoAnterior or imgGradiente[i,j] < vecinoSiguiente:
                imgNSM[i,j] = 0
            else:
                # Validamos con los valores de threshold alto y bajo
                if imgGradiente[i,j] > thresholdAlto:
                    imgNSM[i,j] = imgGradiente[i,j]
                elif imgGradiente[i,j] < thresholdBajo:
                    imgNSM[i,j] = 0
                elif vecinoAnterior > thresholdAlto or vecinoSiguiente > thresholdAlto:
                    imgNSM[i,j] = imgGradiente[i,j]
                else:
                    imgNSM[i,j] = 0

    # Guardamos la nueva imagen
    cv2.imwrite('canny_' + imgName, imgNSM)

    # Mostramos la imagen recien guardada
    newImg = cv2.imread('canny_' + imgName)
    cv2.imshow('Imagen con deteccion de bordes mediante Canny', newImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 


# canny("test_image.JPG")
canny("drums.JPG")
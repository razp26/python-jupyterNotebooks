import cv2
import numpy as np
import sys

def imgBinarization(inImg, umbral):

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
        
    # Procedemos retornar el arreglo con la imagen binarizada
    return outImg


def imgSum(inImg1, inImg2):
    alto1 = inImg1.shape[0]
    ancho1 = inImg1.shape[1]
    canales1 = inImg1.shape[2]

    alto2 = inImg2.shape[0]
    ancho2 = inImg2.shape[1]
    canales2 = inImg2.shape[2]

    alto = alto1 if alto1 > alto2 else alto2
    ancho = ancho1 if ancho1 > ancho2 else ancho2
    
    if (canales1 != canales2):
        raise ValueError('Las imagenes deben tener el mismo numero de canales.')

    if (canales1 > 1):
        imgOut = np.zeros((alto, ancho, canales1))
    else:
        imgOut = np.zeros((alto, ancho))


    for i in range(alto):
        for j in range(ancho):

            if alto1 >= i and ancho1 >= j:
                pixel1 = inImg1[i,j]
            else:
                if canales1 == 1:
                    pixel1 = 0
                else:
                    pixel1 = [0,0,0]

            if alto2 >= i and ancho2 >= j:
                pixel2 = inImg2[i,j]
            else:
                if canales1 == 1:
                    pixel2 = 0
                else:
                    pixel2 = [0,0,0]

            if (canales1 == 1):
                imgOut[i,j] = int(pixel1) + int(pixel2)
                if imgOut[i,j] > 255:
                    imgOut[i,j] = 255
            else:
                pixelAzul = int(pixel1[0]) + int(pixel2[0])
                pixelVerde = int(pixel1[1]) + int(pixel2[1])
                pixelRojo = int(pixel1[2]) + int(pixel2[2])

                if pixelAzul > 255:
                    pixelAzul = 255

                if pixelVerde > 255:
                    pixelVerde = 255

                if pixelRojo > 255:
                    pixelRojo = 255

                imgOut[i,j] = [pixelAzul, pixelVerde, pixelRojo]

    return imgOut



def imgSubs(inImg1, inImg2):
    alto1 = inImg1.shape[0]
    ancho1 = inImg1.shape[1]
    canales1 = inImg1.shape[2]

    alto2 = inImg2.shape[0]
    ancho2 = inImg2.shape[1]
    canales2 = inImg2.shape[2]

    alto = alto1 if alto1 > alto2 else alto2
    ancho = ancho1 if ancho1 > ancho2 else ancho2
    
    if (canales1 != canales2):
        raise ValueError('Las imagenes deben tener el mismo numero de canales.')

    if (canales1 > 1):
        imgOut = np.zeros((alto, ancho, canales1))
    else:
        imgOut = np.zeros((alto, ancho))


    for i in range(alto):
        for j in range(ancho):

            if alto1 >= i and ancho1 >= j:
                pixel1 = inImg1[i,j]
            else:
                if canales1 == 1:
                    pixel1 = 0
                else:
                    pixel1 = [0,0,0]

            if alto2 >= i and ancho2 >= j:
                pixel2 = inImg2[i,j]
            else:
                if canales1 == 1:
                    pixel2 = 0
                else:
                    pixel2 = [0,0,0]

            if (canales1 == 1):
                imgOut[i,j] = int(pixel1) - int(pixel2)
                if imgOut[i,j] < 0:
                    imgOut[i,j] = int(imgOut[i,j]) * -1
            else:
                pixelAzul = int(pixel1[0]) - int(pixel2[0])
                pixelVerde = int(pixel1[1]) - int(pixel2[1])
                pixelRojo = int(pixel1[2]) - int(pixel2[2])

                if pixelAzul < 0:
                    pixelAzul = pixelAzul * -1

                if pixelVerde < 0:
                    pixelVerde = pixelVerde * -1

                if pixelRojo < 0:
                    pixelRojo = pixelRojo * -1

                imgOut[i,j] = [pixelAzul, pixelVerde, pixelRojo]

    return imgOut


def imgsAND(inImg1, inImg2):
    alto1 = inImg1.shape[0]
    ancho1 = inImg1.shape[1]

    alto2 = inImg2.shape[0]
    ancho2 = inImg2.shape[1]

    alto = alto1 if alto1 > alto2 else alto2
    ancho = ancho1 if ancho1 > ancho2 else ancho2
    
    imgOut = np.zeros((alto, ancho))

    for i in range(alto):
        for j in range(ancho):

            if alto1 <= i or ancho1 <= j:
                pixel1 = 0
            else:
                pixel1 = inImg1[i,j]

            if alto2 <= i or ancho2 <= j:
                pixel2 = 0
            else:
                pixel2 = inImg2[i,j]

            if (pixel1 == 255 and pixel2 == 255):
                pixelOut = 255
            else:
                pixelOut = 0

            imgOut[i,j] = pixelOut

    return imgOut



def imgsOR(inImg1, inImg2):
    alto1 = inImg1.shape[0]
    ancho1 = inImg1.shape[1]

    alto2 = inImg2.shape[0]
    ancho2 = inImg2.shape[1]

    alto = alto1 if alto1 > alto2 else alto2
    ancho = ancho1 if ancho1 > ancho2 else ancho2
    
    imgOut = np.zeros((alto, ancho))

    for i in range(alto):
        for j in range(ancho):

            if alto1 <= i or ancho1 <= j:
                pixel1 = 0
            else:
                pixel1 = inImg1[i,j]

            if alto2 <= i or ancho2 <= j:
                pixel2 = 0
            else:
                pixel2 = inImg2[i,j]

            if (pixel1 == 255 or pixel2 == 255):
                pixelOut = 255
            else:
                pixelOut = 0

            imgOut[i,j] = pixelOut

    return imgOut


def imgsXOR(inImg1, inImg2):
    alto1 = inImg1.shape[0]
    ancho1 = inImg1.shape[1]

    alto2 = inImg2.shape[0]
    ancho2 = inImg2.shape[1]

    alto = alto1 if alto1 > alto2 else alto2
    ancho = ancho1 if ancho1 > ancho2 else ancho2
    
    imgOut = np.zeros((alto, ancho))

    for i in range(alto):
        for j in range(ancho):

            if alto1 <= i or ancho1 <= j:
                pixel1 = 0
            else:
                pixel1 = inImg1[i,j]

            if alto2 <= i or ancho2 <= j:
                pixel2 = 0
            else:
                pixel2 = inImg2[i,j]

            if (pixel1 == pixel2):
                pixelOut = 0
            else:
                pixelOut = 255

            imgOut[i,j] = pixelOut

    return imgOut



def imgOperation(imgName1, imgName2, operacion):
    
    img1 = cv2.imread(imgName1)
    img2 = cv2.imread(imgName2)
    
    if operacion == "SUMA":
        imgOut = imgSum(img1, img2)
        imgName = 'suma_img.jpg'
    elif operacion == "RESTA":
        imgOut = imgSubs(img1, img2)
        imgName = 'resta_img.jpg'
    elif operacion == "AND":
        img1_binary = imgBinarization(img1, 90)
        img2_binary = imgBinarization(img2, 90)
        imgOut = imgsAND(img1_binary, img2_binary)
        imgName = 'and_img.jpg'
    elif operacion == "OR":
        img1_binary = imgBinarization(img1, 90)
        img2_binary = imgBinarization(img2, 90)
        imgOut = imgsOR(img1_binary, img2_binary)
        imgName = 'or_img.jpg'
    elif operacion == "XOR":
        img1_binary = imgBinarization(img1, 90)
        img2_binary = imgBinarization(img2, 90)
        imgOut = imgsXOR(img1_binary, img2_binary)
        imgName = 'xor_img.jpg'
    
    # Guardamos la imagen
    cv2.imwrite(imgName, imgOut)

    # Mostramos la imagen recien guardada
    newImg = cv2.imread(imgName)
    cv2.imshow('Imagen resultado', newImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()           

# imgOperation("sum1.jpg", "sum2.jpg", "SUMA")
# imgOperation("subs1.jpg", "subs2.jpg", "RESTA")
# imgOperation("img_and1.jpg", "img_and2.jpg", "AND")
# imgOperation("img_or1.jpg", "img_or2.jpg", "OR")
imgOperation("img_xor1.jpg", "img_xor2.jpg", "XOR")
sys.exit(0)
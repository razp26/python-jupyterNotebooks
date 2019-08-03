import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt

def colorImageHistogram(imgColorFile):
    # Leemos las imagenes recibidas como parametros
    imgColor = cv2.imread(imgColorFile)

    alto = imgColor.shape[0]
    ancho = imgColor.shape[1]
    canales = imgColor.shape[2]

    # Creamos una matriz de pixeles inicializada a cero que se utilizara para unificar la imagen
    listaSalidaVerde = []
    listaSalidaRojo = []
    listaSalidaAzul = []
    listaSalidaGris = []

    # Recorremos las imagenes pixel por pixel
    for i in range(alto):
        for j in range(ancho):
            pixel = imgColor[i,j]
            listaSalidaAzul.append(pixel[0])
            listaSalidaVerde.append(pixel[1])
            listaSalidaRojo.append(pixel[2])
            listaSalidaGris.append(int((int(pixel[0]) + int(pixel[1]) + int(pixel[2]))/3))

    # Guardamos la imagen
    bins = np.linspace(0,255,256)
    plt.hist(listaSalidaAzul, bins, facecolor='blue', alpha=0.5, label='Histograma valores canal AZUL')
    plt.axvline(np.array(listaSalidaAzul).mean(), color = 'blue', linestyle='dashed', linewidth=1)
    plt.legend(loc='upper right')
    plt.savefig('blue_histogram.png')
    plt.clf()

    plt.hist(listaSalidaVerde, bins, facecolor='green', alpha=0.5, label='Histograma valores canal VERDE')
    plt.axvline(np.array(listaSalidaVerde).mean(), color = 'green', linestyle='dashed', linewidth=1)
    plt.legend(loc='upper right')
    plt.savefig('green_histogram.png')
    plt.clf()

    plt.hist(listaSalidaRojo, bins, facecolor='red', alpha=0.5, label='Histograma valores canal ROJO')
    plt.axvline(np.array(listaSalidaRojo).mean(), color = 'red', linestyle='dashed', linewidth=1)
    plt.legend(loc='upper right')
    plt.savefig('red_histogram.png')
    plt.clf()

    plt.hist(listaSalidaGris, bins, facecolor='grey', alpha=0.5, label='Histograma escala GRISES ponderada')
    plt.axvline(np.array(listaSalidaGris).mean(), color = 'grey', linestyle='dashed', linewidth=1)
    plt.legend(loc='upper right')
    plt.savefig('grey_histogram.png')
    plt.clf()

colorImageHistogram("test_image.JPG")
sys.exit()

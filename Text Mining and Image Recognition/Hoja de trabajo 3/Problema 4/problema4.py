import re
import pandas as pd

def main():

    # Leemos el contenido de los archivos y lo almacenamos en el dataframe data
    data  = pd.DataFrame()
    for i in range(1,22):
        filename = 'Datos/D'+ str(i)+ '.txt'
        fileData = pd.read_csv(filename, header = None)
        data = data.append(fileData)
    
    # Definimos la expresion regular a utilizar
    regEx = "(([0]?[1-9]{1}|[1-2][0-9]{1}|[3][0-1]{1})(/|\-|\.){1}([0]?[1-9]{1}|[1][0-2]{1}|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)(/|\-|\.){1}((20)?[0-1][0-9]{1}))$"
    objRegEx = re.compile(regEx)

    # Renombramos la columna del dataframe que tiene las fechas de entrada
    data.columns=['entrada']

    # Inicializamos los contadores
    dias = 0
    meses = 0
    anios = 0
    contador = 0

    for i, r in data.iterrows():
        fecha = objRegEx.match(r['entrada'])
        if fecha:
            contador = contador + 1
            dias = dias + int(fecha.group(2))
            anios = anios + int(fecha.group(6))

            # Procesamos el mes
            numeroMes = 0
            if fecha.group(4) == 'Jan':
                numeroMes = 1
            elif fecha.group(4) == 'Feb':
                numeroMes = 2
            elif fecha.group(4) == 'Mar':
                numeroMes = 3
            elif fecha.group(4) == 'Apr':
                numeroMes = 4
            elif fecha.group(4) == 'May':
                numeroMes = 5
            elif fecha.group(4) == 'Jun':
                numeroMes = 6
            elif fecha.group(4) == 'Jul':
                numeroMes = 7
            elif fecha.group(4) == 'Aug':
                numeroMes = 8
            elif fecha.group(4) == 'Sep':
                numeroMes = 9
            elif fecha.group(4) == 'Oct':
                numeroMes = 10
            elif fecha.group(4) == 'Nov':
                numeroMes = 11
            elif fecha.group(4) == 'Dec':
                numeroMes = 12
            else:
                numeroMes = int(fecha.group(4))

            meses = meses + numeroMes

    # Retornamos los promedios
    return dias/contador, meses/contador, anios/contador


dias, meses, anios = main()
print('Promedio de dia: ', dias)
print('Promedio de mes: ', meses)
print('Promedio de anio: ', anios)


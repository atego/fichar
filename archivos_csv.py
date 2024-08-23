import csv
import datetime

nombres_meses: list = [
    'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
    'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'
]

mes: str = nombres_meses[datetime.date.today().month - 1]

datos: list = []

try:
    with open(file=f'{mes}.csv', mode='r') as archivo_datos:
        dato_leidos = csv.reader(archivo_datos)
        for d in dato_leidos:
            datos.append(d)
except FileNotFoundError:
    archivo_datos = open(file=f'{mes}.csv', mode='x')
    print(f'Se ha creado el archivo {mes}.csv')


print(datos)

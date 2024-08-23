import dataset
import datetime


fecha: datetime = datetime.date.today()
print(type(fecha))
print(fecha)

nombres_meses: list = [
    'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
    'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'
]
# mes: str = nombres_meses[datetime.date.today().month - 1]
mes = 'julio'

db = dataset.connect('sqlite:///dias_fichados.db')
tabla_agosto = db[mes]
# tabla_agosto.insert({'nombre': 'Marga', 'edad': 56, 'profesion': 'Seguros', 'fecha': fecha})

print(db.tables)

# datos: list = []
#
# for d in tabla_agosto:
#     datos.append(
#         (d['nombre'],
#          d['edad'],
#          d['profesion'])
#     )
# print(datos[0][0])

# for nombre in tabla_agosto:
#     print(nombre['nombre'])
#
# m = tabla_agosto.find_one(nombre='Ilde')
# print(m['nombre'], m['edad'])
print(fecha.month)
for r in tabla_agosto.find(fecha={'==': fecha}):
    print(r['nombre'])

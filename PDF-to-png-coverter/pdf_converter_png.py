import os
from wand.image import Image

print("Bienvenido al convertidor de PDF a PNG :3 \n")

nombre_del_pdf = str(input("Digite el nombre del PDF sin la extención: ")+".pdf")
nombre_de_salida = str(input("Digite el nombre de salida del archivo sin la extención: ")+".png")
resolucion = 2000

# Crea una carpeta con el nombre del archivo PDF
nombre_de_carpeta = os.path.splitext(nombre_del_pdf)[0]
if not os.path.exists(nombre_de_carpeta):
    os.makedirs(nombre_de_carpeta)

# Aquí hago que tome al archivo PDF con la resolución resultante que quiero que quede y lo guardo en la variable imagen
with Image(filename=nombre_del_pdf, resolution= resolucion) as imagen:
    # Aquí le cambio el formato
    imagen.format = 'png'
    # Aquí le pido que la guarde en la carpeta creada con el nombre del archivo PDF
    imagen.save(filename=os.path.join(nombre_de_carpeta, nombre_de_salida))

# Indico que fué exitosa la carga :3
print("La conversión ha sido exitosa :3")

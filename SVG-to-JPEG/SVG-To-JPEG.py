import os
from wand.image import Image

# Solicitar el nombre del archivo SVG a convertir
svg_filename = input("Ingrese el nombre del archivo SVG (incluyendo la extensión): ")

# Verificar que el archivo SVG exista
if not os.path.isfile(svg_filename):
    print("El archivo especificado no existe.")
    exit()

# Definir el nombre del archivo de salida JPG
jpg_filename = os.path.splitext(svg_filename)[0] + ".jpg"

# Convertir el archivo SVG a una imagen JPG con la resolución deseada
with Image(filename=svg_filename, resolution=1000) as img:
    img.format = 'jpeg'
    img.save(filename=jpg_filename)

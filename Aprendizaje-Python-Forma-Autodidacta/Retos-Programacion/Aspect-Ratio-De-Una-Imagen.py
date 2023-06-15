'''
/*
 * Crea un programa que se encargue de calcular el aspect ratio de una
 * imagen a partir de una url.
 * - Url de ejemplo: https://raw.githubusercontent.com/mouredev/
 *   mouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
 *   imagen de 1920*1080px.
 */ 
'''

from PIL import Image

def funcion1(rutaimagen, nuevo_ancho, nuevo_alto):
    imagen_ajustada = rutaimagen.resize((nuevo_ancho,nuevo_alto))
    return imagen_ajustada

rutaimagen = './mouredev_github_profile.png'
imagen_original = Image.open(rutaimagen)


nuevo_ancho = 800
nuevo_alto = 600

imagen_ajustada = funcion1('./mouredev_github_profile.png', nuevo_ancho, nuevo_alto)
imagen_ajustada.save('imagen_ajistada.png')

print("Dimensiones de la imagen original", imagen_original.size)
print("Dimensiones de la imagen ajustada", imagen_ajustada.size)

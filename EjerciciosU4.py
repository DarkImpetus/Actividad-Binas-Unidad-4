# -*- coding: utf-8 -*-
import re  # importacion expresion regular

# inicio del archivo que se debe de usar para aplicar la expresion regular
path = "archivo.txt"
codigo = "codigobasico.txt"

# manejo de error para si no se encuentra el archivo
try:
    archivo1 = open(codigo, 'r')
except:
    # por si no se encuentra el archivo
    print("no se encuentra el archivo codigo")
    quit()

muestracodigo = ""

for linea1 in archivo1:
    muestracodigo += linea1


try:
    archivo = open(path, 'r')
except:
    print("El archivo no se encuentra")
    quit()

texto = ""

for linea in archivo:
    texto += linea

#
# para mas informacion de expresion regular se puede buscar en este apartado.7
# link de consulta: https://www.guru99.com/python-regular-expressions-complete-tutorial.html
#
# Variables válidas. Ejemplo: suma, i, cont7, etc.
patronVARIABLES = r'(\b[A-Za-z0-9-_]+\s*[=])+'
# 'r' de espresion regular
# buscar variablas de A-Za-z asi mismo como los numero de 0-9
# '+' diciendole que debe  agregar el otro complento a la primera expresion regular
# asina los resultado a 'resultadoVariables  usnando el patro
# Ejercicio 2

#### e02_01.py : escribe un programa en Python 3 que pida cinco números y que escriba su media aritmética.

print('progresion')

numeros = [7, 8, 9, 10, 11]
suma = 0

for i in numeros:
    suma = suma + i
    
media = suma / 5
print('La media es: ' + str (media))

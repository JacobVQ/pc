José Mría Carrasco;
Hola, vamos a insertar una imagen; 

![Imágen toreo](http://3.bp.blogspot.com/-HvJgDaYLwUU/UdVlGFCAUnI/AAAAAAAAAbg/3Ynpbykfd4Q/s500/1372867763_extras_portadilla_0.jpg)


#Ejercicio 1

##Código en Python

En Markdown puedes poner código de cualquier lenguajes en una misma línea y en bloque:

```python
import random
numero, intento = random.randint(1, 10), 0
while numero != intento:
    intento = int(input('¡Adivina un número del 1 al 10!'))
print('¡Acertaste!')
```
##Pruebas: Calificaciones y CE


Lista no ordenada:

* **CE**: Criterio de Evaluacion.
* **PM**: Puntuación Máxima.
* **PS10**: Puntuación Sobre 10.
* **RA**: Resultado de Aprendizaje.

Esto es un ejemplo de cómo hacer una prueba para la Unidad Didáctica 5 de Seguridad Informática siendo Ésta su table CE-PM de la Programación Didactica:

#####UNIDAD DIDÁCTICA 5-RA5 (PM total:150)
| **CE** | **RA5:a** | **RA5:b** | **RA5:c** | **RA5:d** | **RA5:e** | **RA5:f** |
|-----|------|-------|--------|-------|------|------|
| PM  |  50  |  50   |   10   |  10   |  20  |  10  | 

#####Opción 1 (ideal para pruebas de desarrollo)


| Pregunta | CE | PM |  PS10 |
|--------|-----------|------|------|
| 1  | RA5:a   |  50   |  3.3 |
| 2 | RA5:b |  50  | 3.3 |
| 3 | RA5:c |  10  | 1 |
| 4 | RA5:d |  10   | 1 |
| 5 | RA5:e |  20  | 1.3 |
| 6 | RA5:f |  10  | 1 |
| Total | RA5:a-RA5:f | 150| 10 |

#####Opción 2 (ideal para pruebas y/o combinar CE):


| Pregunta | CE | PM |  PS10 |
|--------|-------|------|-----|
| 1  | RA5:a   |  50   |  3.3 |
| 2 | RA5:b |  50  | 3.3 |
| 3 | RA5:c-RA5:f |  50  | 1 |
| Total | RA5:a-RA5:f | 150| 10 |


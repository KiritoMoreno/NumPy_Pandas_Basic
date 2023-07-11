'''
import numpy as np

list = [1,2,3,4,5,6,7,8,9]
print(list)

arr = np.array(list)
print(arr)
print(type(arr))

matriz = [1,2,3],[4,5,6],[7,8,9]
matriz = np.array(matriz)
print(matriz)

# Index con arrays
print(arr[0])
print(arr[0] + arr[5])

# Index con matrizes
print(matriz[0]) # ingresa a la primera posición de la fila

print(matriz[0,2]) # ingresa a la primera fila y columna

# Slicing Nos permite extraer varios datos, tiene un comienzo y un final.
print(arr[1:6])
print(arr[:6]) # Si no se ingresa el valor de inicio, se toma el inicio como la posición 0.
print(arr[2:]) # En cambio, si no se le da una posición final, se regresan todos los elementos hasta el final del array.

# También se puede trabajar por pasos.
# En este ejemplo de 3 en 3.
print(arr[::3])


Cuando se le asigna un valor negativo se regresan los valores comenzando desde la última posición del array.
arr[-1]
---> 9
arr[-3:]
---> array([7, 8, 9])

Para el caso de las matrices, sucede algo similar.
Para acceder a los valores entre filas.

matriz[1:]
---> array([[4, 5, 6],[7, 8, 9]])

Para acceder a los valores entre filas y columnas.

matriz[1:, 0:2]
---> array([[4, 5],[7, 8]])
'''
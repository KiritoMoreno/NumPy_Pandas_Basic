import numpy as np
'''
scalar = np.array(42)
print(scalar) 
scalar.ndim  # Validamos en numpy

Declarando un vector.
vector = np.array([1, 2, 3])
print(vector) 
vector.ndim # Con que dimensiones estamos trabajando

Declarando una matriz.
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz)
matriz.ndim

Declarando un tensor. Una matrix dentro de otra matrix
tensor = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],[[13, 13, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24]]])
print(tensor)
tensor.ndim

Se puede definir el número de dimensiones desde la declaración del array
vector = np.array([1, 2, 3], ndmin = 10)
print(vector) 
vector.ndim 

Se pueden expandir dimensiones a los array ya existentes con expand_dims(). Axis = 0 hace referencia a las filas, mientras que axis = 1 a las columnas.
expand = np.expand_dims(np.array([1, 2, 3]), axis = 0)
print(expand)
expand.ndim 

Remover/comprimir las dimensiones que no están siendo usadas.
print(vector, vector.ndim) 
vector_2 = np.squeeze(vector)
print(vector_2, vector_2.ndim)

'''
'''
Reto
Definir un tensor de 5D
Sumarle una dimensión en cualquier eje
Borrar las dimensiones que no se usen
'''
matrix = np.array([[1,2,3],[4,5,6]])
print(matrix)
print(matrix.ndim)

matrix = np.array([[1,2,3],[4,5,6]], ndmin = 5)
print(matrix)
print(matrix.ndim)
print("expand -->")
expand =np.expand_dims(matrix, axis = 0 )
print(expand)
print(expand.ndim)
print("Borrar -->")
print(matrix, matrix.ndim) 
vector_2 = np.squeeze(matrix)
print(vector_2, vector_2.ndim)



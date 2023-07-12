# Operaciones
import numpy as np

list = [1,2]
#Una lista de Python entiende que quieres duplicar los datos. No es lo que buscamos.
list = list * 2

#Pero Numpy lo entiende mucho mejor
arr=np.arange(0,10)
print(arr)
arr2 = arr.copy()

#Ahora multiplicamos por un vector:
print(arr*2)

# Operación suma de vectores:
print(arr+2)

#División con un vector
#Como en este caso la primera posición del array es 0, muestra un error pero, no detiene el proceso.
print(1 / arr)
#---> RuntimeWarning: divide by zero encountered in true_divide
# """Entry point for launching an IPython kernel.

#Elevar a un vector:
print(arr **2)

#Sumar dos arrays de igual dimensiones las hace elemento por elemento:
print(arr + arr2)

#Lo mismo aplica para matrices.
matriz = arr.reshape(2,5)
matriz2 = matriz.copy()
print(matriz)
print()
#Una operación importante es la de punto por punto, aquí dos formas de hacerla:
print(np.matmul(matriz, matriz2.T))
print("")
print(matriz @ matriz2.T)
# .copy  con NumPy

import numpy as np


#.copy() nos permite copiar un array de NumPy en otra variable de tal forma que al modificar el nuevo array los cambios no se vean reflejados en array original.

arr = np.arange(0, 11)
print(arr)

#Tomamos un trozo del array original
print(arr[0:6])
trozo_de_arr = arr[0:6]
print(trozo_de_arr)

#Queremos pasar todas nuestras variables a 0
trozo_de_arr[:] = 0

#Se han modificado los datos del array original porque seguía haciendo referencia a esa variable.
print(arr)

#Con .copy() creamos una copia para no dañar nuestro array original
arr_copy = arr.copy()
arr_copy[:] = 100
print(arr_copy)

#Esta función te ayudará a prevenir muchos errores y tener más confianza a la hora de manipular los datos


# Condiciones con NumPy
import numpy as np

arr = np.linspace(1,10,10, dtype = 'int8')
print(arr)

#Regresa un array de booleanos dónde la condición se cumple.

indices_cond = arr > 5
print(indices_cond)

#Regresa los valores para dónde la condiciones True.

print(arr[indices_cond])

#Múltiples condiciones.
print(arr[(arr > 5) & (arr < 9)])

#Modificar los valores que cumplan la condición.

arr[arr > 5] = 99
print(arr)

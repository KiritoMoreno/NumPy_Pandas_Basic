import numpy as np

'''
Shape
Indica la forma del arreglo.
arr = np.random.randint(1,10,(3,2))
print(arr.shape)

Reshape
transforma el arreglo mientras se mantengan los elementos.
print(arr.reshape(1,6))
print(arr.reshape(2,3))
print(np.reshape(arr,(1,6))) # Funciona de la misma forma que las anteriores

Se puede hacer un reshape como lo haría C. va desde fila a fila
print(np.reshape(arr,(2,3), 'C'))

También se puede hacer reshape a como lo haría Fortran. va desde columna a columna
print(np.reshape(arr,(2,3), 'F'))

Además, existe la opción de hacer reshape según como esté optimizado nuestro computador. En este caso es como en C.
print(np.reshape(arr,(2,3), 'A')) # Elige la mejor opción "C" o "F"

"No puedes cambiar la "forma" a la "forma" original del array, si tienes un (3,3) no lo puedes pasar a (4,2). 
No respeta los 9 elementos del array original"

Reto
Crear un array de cualquier dimensión y cambiar sus dimensiones.
Intenta cambiar el array de forma que no respete la estructura original
'''
arr = np.random.randint(1,20,(4,2))
print(arr.shape)
print(arr)
print("Cambiando sus dimensiones-->")
print(np.reshape(arr,(2,4)))
print("No respeta la est.original-->")

# np.reshape(arr,(4,4), 'C')


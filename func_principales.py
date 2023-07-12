# Funciones principales con numpy
import numpy as np
'''
arr = np.random.randint(1, 20, 10)
print(arr)

matriz = arr.reshape(2,5)
print(matriz)

.max Para el máximo
print(arr.max()) 
print(matriz.max())

Podemos regresar los máximos de cada fila o columna especificando el eje
print(matriz.max(1))
print(matriz.max(0))

También tenemos .argmax() que nos devuelve la posición del elemento(el indice)
print(arr.argmax())

En el caso de la matriz nos muestra con un 1 dónde se encuentra el mayor entre las columnas
print(matriz.argmax(0))

De forma análoga tenemos .min()
print(arr.min())
print(arr.argmin())
print(matriz.min(0))
print(matriz.argmin(1))

Podemos saber la distancia entre el valor más bajo con el más alto.
print(arr.ptp()) # 17 - 3 ---> 14
print(matriz.ptp(0)) #---> array([11,  4,  8,  0,  6])

Análisis estadístico
Ordenar los elementos:
print(arr.sort()) #---> array([ 3,  6,  7,  7,  9, 11, 12, 12, 15, 17]))

Obtener un percentil: nos puede dar 3 opciones el min, la mediana o el max
print(np.percentile(arr, 50)) 

Mediana:
print(np.median(arr))

Desviación estándar:
print(np.std(arr))

Varianza:
print(np.var(arr))

Promedio:
print(np.mean(arr))

Lo mismo aplica para las matrices.
print(np.median(matriz, 1))

Concatenación
Se pueden unir dos arrays
a = np.array([[1,2], [3,4]])
b= np.array([5, 6])
print(np.concatenate((a,b), axis = 0))

---> ValueError: all the input arrays must have same number of dimensions, but the array at index 0 has 2 dimension(s) and the array at index 1 has 1 dimension(s)
El error anterior es debido a que 'a' tiene 2 dimensiones, mientras que 'b' tiene 1.

print(a.ndim) #---> 2
print(b.ndim) #---> 1

Debemos poner 'b' en 2 dimensiones también.
b = np.expand_dims(b, axis = 0)
print(np.concatenate((a,b), axis = 0))

De igual manera, podemos agregarlo en el otro eje
print(np.concatenate((a,b), axis = 1))

ValueError: all the input array dimensions for the concatenation axis must match exactly, but along dimension 0, the array at index 0 has size 2 and the array at index 1 has size 1
Como 'b' es una fila y no una columna, no se puede concatenar a menos que se aplique la transpuesta.

La transpuesta pone nuestro array en sentido opuesto, si el array original es (1,2), con la transpuesta quedará (2,1)
(b.T)

print(np.concatenate((a,b.T), axis = 1))



'''
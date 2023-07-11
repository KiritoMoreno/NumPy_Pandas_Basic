import numpy as np
'''
list (range(0,10))
print(list)
# Ahora con NumPy -->
print(np.arange(0,10))

Un tercer argumento permite definir un tamaño de paso.
print(np.arange(0,20,2))

np.zeros() Nos permite definir estructuras o esquemas.
print(np.zeros(3))
print(np.zeros((10,5))) # un array de tipo matricial

De igual manera, tenemos np.ones()
print(np.ones(3))

np.linspace() Permite generar una array definiendo un inicio, un final y cuantas divisiones tendrá.
print(np.linspace(0, 10 , 10))

También podemos crear una matriz con una diagonal de 1 y el resto de 9.
print(np.eye(4))

Otro método importante es generar números aleatorios.
print(np.random.rand())

También se pueden generar vectores.
print(np.random.rand(4))

Y a su vez generar matrices.
print(np.random.rand(4,4))

NumPy nos permite también generar números enteros.
En este caso números enteros entre el 1 y 14
print(np.random.randint(1,15))

También podemos llevarlos a una estructura definida.
print(np.random.randint(1,15, (3,3)))


'''
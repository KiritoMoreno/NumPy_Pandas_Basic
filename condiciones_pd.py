# Filtrado por condiciones con Pandas
import pandas as pd

#Llamamos los datos de un archivo csv para manejarlos
df_books = pd.read_csv('bestsellers-with-categories.csv')
df_books.head(2) 

#Mostrar datos que sean mayores a cierto valor
mayor_a_2016 =df_books['Year'] > 2016
#print(mayor_a_2016)

#Filtrar datos en nuestro DataFrame que sean mayores a cierto valor
df_books[mayor_a_2016]

#También se puede colocar la condición directamente como parámetro
df_books[df_books['Year'] > 2016]

#Mostrar los datos que sean igual a cierto valor
genreFiction = df_books['Genre'] == 'Fiction'
#print(genreFiction)

#Filtrado con varias condiciones
print(df_books[genreFiction & mayor_a_2016])

#Filtrado con negación
print(df_books[~mayor_a_2016])



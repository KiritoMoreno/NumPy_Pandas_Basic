#Series y DataFrames en Pandas
import pandas as pd

#Series
#Es un arreglo unidimensional indexado
#Definiendo una lista con índices específicos
psg_players = pd.Series(['Navas','Neymar','Messi'], index =[1,7,10,30])
print(psg_players)

#Búsqueda por índices mediante un diccionario
dict = {1: 'Navas', 7: 'Mbappe', 10: 'Neymar', 30:'Messi'}
print(pd.Series(dict))

#Búsqueda mediante Slicing
print(psg_players[0:3])

#Pandas
#Similar a la estructura matricial
dict = {'Jugador':['Navas','Mbappe','Neymar','Messi'],
 'Altura':[183.0, 170.0, 170.0, 163.0],
  'Goles':[2, 200, 150, 500]}

df_players = pd.DataFrame(dict, index=[1,7,10,30])
print(df_players)
#Búsqueda por índices. Columnas
print(df_players.columns)

#Búsqueda por índice.
print(df_players.index)

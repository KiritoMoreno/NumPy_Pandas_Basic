# JOIN
#Join Es otra herramienta para hacer exactamente lo mismo, una combinación. La diferencia es que join va a ir a los índices y no a columnas específicas.
import pandas as pd
import numpy as np

izq = pd.DataFrame({'A': ['A0','A1','A2'],
  'B':['B0','B1','B2']},
  index=['k0','k1','k2'])

der =pd.DataFrame({'C': ['C0','C1','C2'],
  'D':['D0','D1','D2']},
  index=['k0','k2','k3'])

#Combinamos izq con der (Directamente del index)
izq.join(der)

#Traer todos los datos aunque no hagan match.
izq.join(der, how = 'outer')

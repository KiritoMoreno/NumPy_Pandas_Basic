#Crea tus propios DataFrames, con los índices que quieras y comparte tus resultados.

import pandas as pd

def run():
    granada = {'Jugador':['Luis Suárez','Jorge Molina', 'Antonio Puertas', 'Germán Sánchez', 'Luis Milla', 'Luís Manuel Arantes Maximiano'],
               'Posiciòn':['Delantero', 'Delantero', 'Centrocampista', 'Defensa', 'Centrocampista', 'Portero'],
               'Número':[9, 23, 10, 6, 5, 1],
               'Altura':[185.0, 187.0, 185.0, 187.0, 175.0, 190.0],
               'Goles':[7, 7, 5, 2, 2, 0]
    }

    df_players = pd.DataFrame(granada)
    print(df_players)


if __name__ == "__main__":
    run()
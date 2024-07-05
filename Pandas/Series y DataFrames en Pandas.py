import pandas as pd
psg_players = pd.Series(['Navas','Mbappe','Neymar','Messi'], index=[1,7,10,30])

# print(psg_players)



# Búsqueda por índices
# dict = {1: 'Navas', 7: 'Mbappe', 10: 'Neymar', 30:'Messi'}
# y=pd.Series(dict)
# print(y)

# print(psg_players[7])

# Búsqueda mediante Slicing

# print(psg_players[0:3])

# Similar a la estructura matricial

dict = {'Jugador':['Navas','Mbappe','Neymar','Messi'],
 'Altura':[183.0, 170.0, 170.0, 163.0],
  'Goles':[2, 200, 150, 500]}

df_players = pd.DataFrame(dict)

print(df_players)

# Búsqueda por índices. Columnas

# o=df_players.columns
# print(o)
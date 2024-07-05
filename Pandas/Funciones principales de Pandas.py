import pandas as pd

i=pd.read_csv('C:/Users/Aprendiz/Documents/Curso/archivo.csv',sep=',',header=0)

# print(i.info())
# print(i.describe())
# print(i.tail(2))
# print(i.memory_usage(deep=True))
# print(i['Author'].value_counts())

i=pd.concat([i,i.iloc[0]])

# print(i)

print(i.drop_duplicates())
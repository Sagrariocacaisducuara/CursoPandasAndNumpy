import pandas as pd
import numpy as np
i=pd.read_csv('C:/Users/Aprendiz/Documents/Curso/archivo.csv',sep=',',header=0)




# print(i.drop('Genre',axis=1,))

# i=i.drop('Genre',axis=1,)
# print(i)

# print(i.head(2))

# print(i.drop(range(0,10),axis=0).head(2))

# i['nueva columna']= np.nan
# print(i)
# data=np.arange(0,i.shape[0])
# i['rango']= data
# print(i)


#Agrega colunmas
i=pd.concat([i,i], ignore_index=True)
print(i)

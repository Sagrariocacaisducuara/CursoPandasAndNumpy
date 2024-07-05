import pandas as pd
import numpy as np

dict= {'col1':[1,2,3,np.nan],
       'col2':[4,np.nan,6,7],
       'col3':['a','b','c',None]
       }

df = pd.DataFrame(dict)

# print(df)

# print(df.isnull())

# print(df.isnull() *1)


# print(df.fillna('Mising'))

# print(df.fillna(df.mean))


#Asume el orden del primero teniedo en cuenta que estan estructurados con una serie y frecuencia exacta 
print(df.interpolate())


#elimina los valores nulos 

print(df.dropna())
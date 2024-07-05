import pandas as pd
import numpy as np
i=pd.read_csv('C:/Users/Aprendiz/Documents/Curso/archivo.csv',sep=',',header=0)


t=i[i['Year'] > 2016]
print(t,i)





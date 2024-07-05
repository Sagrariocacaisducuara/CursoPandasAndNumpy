import pandas as pd
i = pd.read_csv('C:/Users/Aprendiz/Documents/Curso/archivo.csv',sep=',',header=0)



# print(i[['Name','Author']])

# print(i.loc[0:4, ['Name','Author']])



#Saber si un dato esta 

# print(i.loc[:,['Author']] == 'JJ Smith')


##ILOC

# print(i.iloc[:,0:3])


print(i.iloc[1,3] * -1)
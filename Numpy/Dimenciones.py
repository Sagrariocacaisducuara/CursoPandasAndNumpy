import numpy as np

#scalar de 0 dimenciones
scalar=np.array(42)
scalar.ndim
#print(scalar)
#print(scalar.ndim)


#vector de 1 dimencion
vector=np.array([1,2,3])
vector.ndim
#print(vector)
#print(vector.ndim)


#matriz de 2 dimenciciones
matriz=np.array([[1,2,3],[4,5,6]])
matriz.ndim
#print(matriz)
#print(matriz.ndim)



# Crear un tensor con listas de igual longitud con 3 dimenciones
tensor = np.array([[[1,2,3],[4,5,6],[7,8,9]], [[10,11,12],[13,14,15],[16,17,1]]])
print(tensor)
print(tensor.ndim)


#Agregar o eliminar dimenciones

vector=np.array([1,2,3],ndmin=10)
vector.ndim
#print(vector)
#print(vector.ndim)


#print(vector, vector.ndim)
vector_2 = np.squeeze(vector)
#print(vector_2,vector_2.ndim)




expand=np.expand_dims(np.array([1,2,3]),axis=0)
#print(expand)
#print(expand.ndim)


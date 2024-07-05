import numpy as np

arr=np.random.randint(1,20,10)
matriz=arr.reshape(2,5)

#print(matriz)
print(arr)

t=matriz.max(1)
#print(t)

#array=arr.min()
#print(array)

u=arr.argmax()
#print(u)

y=np.ptp(matriz[0])
#print(y)

t=np.percentile(matriz,0)
#print(t)

r=np.sort(arr)
#print(r)


y=np.median(arr)
#print(y)

h=np.median(matriz,1)
#print(h)

i=np.std(arr) **2
#print(i)


j=np.var(arr)
#print(j)

k=np.mean(arr)
#print (k)

a= np.array([[1,2],[3,4]])
b= np.array([[5,6]])
t=np.concatenate((a,b),axis=0)
#print(t)


l=np.concatenate((a,b.T),axis=1)
#print(l)

g=b.T
print(g)
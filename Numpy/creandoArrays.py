import numpy as np

list(range(0,10))
#print(list)

array=np.arange(0,10,2)
#print(array)


arrayZ=np.zeros((10,10))
#print(arrayZ)

arrayO=np.ones((10,10))
#print(arrayO)

arrayLin=np.linspace(0,10,10)
#print(arrayLin)

arrayEye=np.eye(4)
#print(arrayEye)


#genera numeros aleatorias
arrayRandom=np.random.rand(4,4)
#print(arrayRandom)



#genera numeros enteros aleatorias
#arrayRandomInt=np.random.randint(1,15)
arrayRandomInt=np.random.randint(1,100,(10,10))
print(arrayRandomInt)


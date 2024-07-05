import numpy as np

random = np.random.randint(1,10,(3,2))
Arr=random.shape
Arr=random.reshape(2,3)
#print(random)
#print(Arr)


arr=np.reshape(random,(2,3),'C')
print(arr)


arr=np.reshape(random,(2,3),'F')
print(arr)


arr=np.reshape(random,(2,3),'A')
print(arr)

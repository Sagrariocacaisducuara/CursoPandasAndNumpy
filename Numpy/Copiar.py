import numpy as np

arr=np.arange(0,11)


trozo=arr[0:6]
#print(trozo)


trozo[:]=0
#print(trozo)

#print(arr)


copy=arr.copy()

copy[:]=100
#print(copy)


arr=np.random.randint(1,10,100)
print(arr)
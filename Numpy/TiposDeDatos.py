import numpy as np

arr=np.array([1,2,3,4])
#print(arr.dtype)


arr=np.array([1,2,3,4], dtype='float64')
#print(arr)


arr = np.array([0,10,2,3,4])
arr = arr.astype(np.bool_)

#print(arr)

'''arr = np.array([0,10,2,3,4])
arr = arr.astype(np.string_)'''#vota error

#print(arr)

arr = np.array(['0','1','2','3','4'])
arr = arr.astype(np.int8)
print(arr)
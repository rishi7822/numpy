#Shape of an Array
#The shape of an array is the number of elements in each dimension.

#Get the Shape of an Array
#NumPy arrays have an attribute called shape that returns a tuple with each index having the number of corresponding elements.
import numpy as np
arr = np.array([[1,2,3,45,5],[22,55,66,777,1]])
print(arr.shape)


#nadmin
#The NumPy ndmin() function allows us to specify the minimum number of dimensions that the resulting array should have.
import numpy as np
arr = np.array([1,2,34,5,6,7],ndmin=6)
print(arr)
print("shape of array:",arr.shape)
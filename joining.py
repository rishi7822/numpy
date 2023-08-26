#Joining means putting contents of two or more arrays in a single array.
#We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis. If axis is not explicitly passed, it is taken as 0.


# import numpy as np

# arr1 = np.array([1,2,3,4])

# arr2 = np.array([21,32,44,11])


# newarr = np.concatenate((arr1,arr2))

# print(newarr)


# #If axis is not explicitly passed, it is taken as 0.
# #join 2 
# import numpy as np

# arr1 = np.array([[1,3,4,4],[2,4,1,1]])

# arr2 = np.array([[11,22,33,44],[55,66,88,99]])

# newarr = np.concatenate((arr1,arr2),axis=1)

# print(newarr)


#using the stack function
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print(arr)


#NumPy provides a helper function: hstack() to stack along rows

import numpy as np

arr1 = np.array([22,33,44,55])

arr2 = np.array([21,23,34,45])


newarr = np.hstack((arr1,arr2))


#NumPy provides a helper function: vstack()  to stack along columns.

import numpy as np

arr1 = np.array([22,33,44,55])

arr2 = np.array([21,23,34,45])


newarr = np.vstack((arr1,arr2))

print(newarr)



#NumPy provides a helper function: dstack() to stack along height, which is the same as depth.

import numpy as np

arr1 = np.array([22,33,44,55])

arr2 = np.array([21,23,34,45])


newarr = np.dstack((arr1,arr2))

print(newarr)


#iterating means going through elements one by one
#As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.

#If we iterate on a 1-D array it will go through each element one by one.
# import numpy as np
# arr = np.array([1,2,3])

# for x in arr:
#     print(x)


# #iterte 2d array it will go through the row one by one
# import numpy as np
# arr = np.array([[1,2,3,4],[2,34,5,66]])

# for x in arr:
#     print(x)

#If we iterate on a n-D array it will go through n-1th dimension one by one
#for reading elem by elem
# import numpy as np
# arr = np.array([[1,2,3,4],[23,34,56,77]])

# for x in arr:
#     for y in x:
#         print(y)


# #iterating for 3d arrays
# #reading elm by elm
# import numpy as np
# arr = np.array([[[1,3,4,5],[12,33,11,22],[333,444,555,666]]])

# for x in arr:
#     for y in x:
#         for z in y:
#             print(z)







#Iterating Arrays Using nditer()
#The function nditer() is a helping function that can be used from very basic to very advanced iterations. It solves some basic issues which we face in iteration, 
#lets go through it with examples


import numpy as np

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
    print(x)




#Iterating Array With Different Data Types
#We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.

#NumPy does not change the data type of the element in-place (where the element is in array) so it needs some other space to perform this action, that extra space is called buffer, and in order to enable it in nditer() we pass flags=['buffered'].

import numpy as np

arr = np.array([1,2,3])

for x in np.nditer(arr, flags=["buffered"], op_dtypes=["S"]):
    print(x)


#Iterating With Different Step Size
#We can use filtering and followed by iteration.

import numpy as np
arr = np.array([[1,2,3,4],[4,53,211,11]])

for x in np.nditer(arr[:,::2]):
    print(x)





#Enumerated Iteration Using ndenumerate()
#Enumeration means mentioning sequence number of somethings one by one.

#Sometimes we require corresponding index of the element while iterating, the ndenumerate() method can be used for those usecases.


import numpy as np

arr = np.array([1,2,3,4,5,6,7,8])

for idx, x in np.ndenumerate(arr):
    print(idx,x)

#for 2d array

import numpy as np

arr = np.array([[1,2,3,4],[1,22,33,44]])

for idx, x in np.ndenumerate(arr):
    print(idx,x)
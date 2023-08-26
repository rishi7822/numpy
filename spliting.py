#splitting is reverse operation of joining
#splitting breaks one array into multiple

#we use array_split() for splitting arrays we pass we wnat to split and numb of splits

#split the arrays into parts

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])

newarr = np.array_split(arr,3)

print(newarr)



#he return value of the array_split() method is an array containing each of the split as an array.

#If you split an array into 3 arrays, you can access them from the result just like any array element:

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])

newarr = np.array_split(arr,3)

print(newarr[0])
print(newarr[1])
print(newarr[2])



#Use the same syntax when splitting 2-D arrays.

#Use the array_split() method, pass in the array you want to split and the number of splits you want to do.

import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)


#Split the 2-D array into three 2-D arrays along rows.

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)

print(newarr)


#An alternate solution is using hsplit() opposite of hstack()

#Use the hsplit() method to split the 2-D array into three 2-D arrays along rows.

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.hsplit(arr,3)

print(newarr)


#Note: Similar alternates to vstack() and dstack() are available as vsplit() and dsplit().
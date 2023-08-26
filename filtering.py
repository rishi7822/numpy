#creating and filtering array
#Filtering Arrays
#Getting some elements out of an existing array and creating a new array out of them is called filtering.

#In NumPy, you filter an array using a boolean index list.


# import numpy as np

# arr = np.array([41, 42, 43, 44])

# x = [True, False, True, False]

# newarr = arr[x]

# print(newarr)


# import numpy as np

# arr = np.array([2,4,5,6,8,10,11])

# #create an empty arr
# filter_arr =[]

# #go through each array
# for element in arr:
#     if element % 2 == 0:
#         filter_arr.append(True)
#     else:
#         filter_arr.append(False)

# newarr = arr[filter_arr]

# print(newarr)





#Creating Filter Directly From Array


#We can directly substitute the array instead of the iterable variable in our condition and it will work just as we expect it to.


#Create a filter array that will return only values higher than 42:

import numpy as np

arr = np.array([1,22,32,43,51,6,71])

filter_arr = arr > 23

newarr = arr[filter_arr]


print(newarr)



#even\\
import numpy as np
arr1 = np.array([22,33,11,33,222,111,2222])

filter_arrr = arr % 2 == 0

newarr = arr1[filter_arrr]

print(newarr)
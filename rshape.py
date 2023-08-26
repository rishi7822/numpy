# #Reshaping arrays
# #Reshaping means changing the shape of an array.

# #The shape of an array is the number of elements in each dimension.

# #By reshaping we can add or remove dimensions or change number of elements in each dimension.

# #Reshape From 1-D to 2-D
# import numpy as np
# arr = np.array([1,2,3,4,5,6,7,8,9,10,100,111,222,22,12])

# newarr = arr.reshape(5,3)

# print(newarr)


# #reshape from 1d to 3 d
# import numpy as np
# arr = np.array([1,2,3,4,5,6,6,88,11,223,3,45,6,7,88,110])

# newarr = arr.reshape(2,4,2)

# print(newarr)




# #returns copy or view

# import numpy as np
# arr = np.array([12,34,11,23,44,5,51,11])

# print(arr.reshape(2,4).base)



#Unknown Dimension
#You are allowed to have one "unknown" dimension.

#Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.

#Pass -1 as the value, and NumPy will calculate this number for you.
# import numpy as np
# arr = np.array([2,3,4,5,6,7,8,9])

# newarr = arr.reshape(2,2,-1)
# print(arr)
# print(newarr)
#We can not pass -1 to more than one dimension.

#array reshaping 
#we can convert a 2d array into a 1d array
import numpy as np
arr = np.array([[1,2,3,4],[23,55,66,77]])

newarr = arr.reshape(-1)

print(newarr)


#convert a 3d into 1d or 2d
import numpy as np
arr = np.array([[[1,2,3,4],[2,34,5,5],[2,34,44,22]]])


newarr = arr.reshape(-1)

print(newarr)
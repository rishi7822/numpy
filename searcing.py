#searching 
#you can search an array for a certain value and return the indexes that get a match
#we can use the where() method


# import numpy as np
# arr = np.array([1,2,3,4,5,1,2,1,1,1])

# x = np.where(arr==1)

# print(x)


# ###another one


# import numpy as np
# arr = np.array([1,2,1,34,5,22,11,29,99,92,29])

# x = np.where(arr==29)

# print(x)



# ####to find the number which is only even 
# import numpy as np

# arr = np.array([1,2,3,4,5,6,22,11,24,34])

# x = np.where(arr%2 == 0)

# print(x)


# ## to find the  number which is only odd

# import numpy as np

# arr = np.array([2,3,4,6,8,10,12,14,16])

# x = np.array(arr%2 == 1)

##############################

#  SEARCHSORTED()

#There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.

#The searchsorted() method is assumed to be used on sorted arrays.

import numpy as np

arr = np.array([2,4,1,7,8])

x = np.searchsorted(arr,1)

print(x)


#searching from right side

import numpy as np
arr = np.array([2,4,6,8,10])

x = np.searchsorted(arr,9,side="right")
print(x)


#using it for multiple numbers



import numpy as np

arr = np.array([2,4,6,8,10])

x = np.searchsorted(arr,[1,3,5,9])

print(x)



#another onee

import numpy as np

arr = np.array([1,3,6,9])

x = np.searchsorted(arr,[2,5,8])

print(x)
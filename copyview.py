# # import numpy as np
# # arr = np.array([2,45,5,6,6,22])
# # x  = arr.copy()
# # arr[0]= 12
# # print(arr)
# # print(x)

# # #Make a view, change the original array, and display both arrays:
# # import numpy as np
# # arr = np.array([2,43,11,22,33,11,33])
# # x = arr.view()
# # arr[0] = 122
# # print(arr)
# # print(x)


# import numpy as np
# arr = np.array([1,23,411,33,11])
# x = arr.sort()
# print(arr)

# print(x)
#Check if Array Owns its Data
#As mentioned above, copies owns the data, and views does not own the data, but how can we check this?

#Every NumPy array has the attribute base that returns None if the array owns the data.

#Otherwise, the base  attribute refers to the original object.
import numpy as np
arr = np.array([1,23,43,56,67])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)
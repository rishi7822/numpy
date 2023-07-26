# # # # # # # # import numpy as np
# # # # # # # # arr = np.array([1,2,4,5,6,7,8])
# # # # # # # # print(arr[4])


# # # # # #u can add these two arrays using indexing also
# # # # # import numpy as np
# # # # # arr = np.array([1,34,5,655,7,87,56])
# # # # # print(arr[2] + arr[3])

# # # # #accesing 2d arrays
# # # # import numpy as np
# # # # arr = np.array([[2,34,56,7],[23,55,672,22]])
# # # # print("2nd elemenT in first row:",arr[0,1])


# # # import numpy as np
# # # arr = np.array([[1,2,45,6,7],[3,55,66,77,78]])
# # # print("4 element in 1st row:",arr[0,3])




# # #accessing 3d arrays
# # import numpy as np
# # arr = np.array([[[2,4,6],[233,56,7],[2,4,5],[24,66,77]]])
# # print(arr[0,3,2])

# #negative indexing 
# import numpy as np
# arr = np.array([[0,1,2],[2,4,5]])
# print(arr[1,-1])


import numpy as np
arr = np.array([[[1,2,3,4,5],[6,7,8,9,10],[23,45,22,11,111]]])
print(arr[0,2,-2])
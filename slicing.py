#Slicing in python means taking elements from one given index to another given index.

#We pass slice instead of index like this: [start:end].

#We can also define the step, like this: [start:end:step].

#If we don't pass start its considered 0

#If we don't pass end its considered length of array in that dimension

#If we don't pass step its considered 1


import numpy as np
arr = np.array([1,3,5,6,7,88,99])
print(arr[1:5])


import numpy as np
arr = np.array([1,4,5,62,11,223,34])
print(arr[:3])


#negative slicing
import numpy as np
arr = np.array([2,4,5,21,33])
print(arr[-1:-3])


#start:end:step

import numpy as np
arr = np.array([34,67,78,99,22,44,55,66])
print(arr[1:3:5])


#reversing
import numpy as np
arr = np.array([12,3,4,5,52,2,3])
print(arr[::2])


#slicing 2d arrays


import numpy as np
arr = np.array([[1,2,4,5,6,7],[12,3,45,66,6,11]])
print(arr[0,1:4])
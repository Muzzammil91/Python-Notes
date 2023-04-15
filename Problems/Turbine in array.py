# make a 5X5 array with 1 on outside dimensions then 0 on inside dimensions then 7 in Center.

import numpy as np

final_arr = np.ones((5, 5), dtype='int32')
ones_arr = np.zeros((3, 3),  dtype='int32')

final_arr[1:-1, 1:-1] = ones_arr

final_arr[2, 2] = 7

print(final_arr)

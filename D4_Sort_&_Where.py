import numpy as np

##sorting

a1 = np.array([2,4,5,44,3,22,6,77,3,2,4])
print('a1 == ', a1, '\n')

a2 = np.array([[[1,2,3], [33,4,56], [3,5,7]]])
print('a2 == \n', a2, '\n')

# print('sorted a1 == ', np.sort(a1, axis = 0), '\n')
# print('sorted a2 ==\n', a2.ndim, a2.size, a2.shape, np.sort(a2, axis = 1), '\n')

# print('a1 == ', a1, '\n')
# print('a2 == \n', a2, '\n')

##Filter

even_num = a1[a1 % 2 == 0]
print(np.sort(even_num))

mask_even_num =  (a1 > 5) & (a1 % 2 == 0)
print(np.sort(a1[mask_even_num]))

where_odd_num = np.where(a1 % 2 == 1)
print(a1[where_odd_num])

ind = [3,4,5,6]
print(a1[ind])
print(a1[[3,4,5,6]])


#where method creates a array with given conditions
#works like if else ::  np.where(if_condtion, what_if_true, else)

condition_array1 = np.where(a1 > 5, a1*2, a1)
print('This is condition_array1::  ', condition_array1)

condition_array2 = np.where(a2%2, 'True', 'False')
print('This is condition_array:2:  \n', condition_array2)
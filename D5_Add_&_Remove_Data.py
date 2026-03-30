import numpy as np

a1 = np.array([15,34,23])
a2 = np.array([28,49,22])
a3 = np.array([78,439,282, 30])

add_1 = a1 + a2     #add the corresponding elements
print(add_1)

# add_2 = a1+a3     raise different shape error
# print(add_2)

concatenate_1 = np.concatenate((a1,a2)) #give parameters as tuple
concatenate_2 = np.concatenate((a1,a2,a3))
print(concatenate_1)
print(concatenate_2)

# x= len(concatenate_2)==np.size(concatenate_2)
# print(type(x), x)

# for i in range(0, np.size(concatenate_2)):
#     print(concatenate_2[i])

## Adding a new row in a array
org_arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
new_row1 = np.array([10,11,12])
new_row2 = np.array([[10,11,12]])
new_column = np.array([[10],[11],[12]])

#checking equality elements wise and return boolean array
print(new_row1 == new_row2)

#for checking entire array eqality use equal() method
print(np.array_equal(new_row2,new_row1))

print(org_arr.ndim, new_row1.ndim, new_column.ndim)

#checking for the same dimension
print(org_arr.shape == new_row1.shape)
print(org_arr.shape == new_column.shape)

arr_with_new_row1  = np.vstack((org_arr, new_row1))   #values in tuple with same number of the columns of the parameter arrays
arr_with_new_row2  = np.vstack((org_arr, new_row2))
arr_with_new_column = np.hstack((org_arr, new_column))   #values in tuple with same number of the rows of the paramerter arrays

print('Checking for the equality of the arrays: ', arr_with_new_row2 == arr_with_new_row1)

print('arr_with_new_row1 : \n', arr_with_new_row1)
print('arr_with_new_row2 : \n', arr_with_new_row2)
print('arr_with_new_column : \n', arr_with_new_column)

##delete method ::: syntax ::: np.delete(array, index or list of indices, axis)     
# axis = None :: (default) delter elements form the flattened array(1d view)
# axis = 0 delete row 
# axis = 1 delete column

arr = np.array([1,2,4,45,67,54,3])
print(np.delete(arr,4))
print(arr)
print('This is deleted array of arr_with_new_column\n',np.delete(arr_with_new_column,3, axis = 1))
print('This is deleted array of arr_with_new_row\n',np.delete(arr_with_new_row2,3, axis = 0))
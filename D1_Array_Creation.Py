import numpy as np
import time

one_dim_matrix = np.array((1,2,3,4))
print('this is one_dim_matrix',  one_dim_matrix)

two_dim_matrix = np.array([[1,2,3,4],
                           [1,2,3,4]])
print(two_dim_matrix)
print(one_dim_matrix.ndim)

start_time = time.time()
lis = [i*2 for i in range(10000)]
print(f'Time take = {time.time()-start_time}')

start_time1 = time.time()
lis = np.arange(10000)*2
print(f'Time take = {time.time()-start_time1}')

#Don't know why everytime list computation comes out to be fast

#zero metrix
zero_metrix = np.zeros((3,4))
print(zero_metrix)

#one metrix
one_matrix = np.ones((3,4))
print(one_matrix)

full_f = np.full((3,3),7)   #first argument () take the shape of matrix and then value to be filled
print(full_f)

#np provide the random module
random_f = np.random.random((2,3))
print(f'ramdom array = {random_f}')

arange_f = np.arange(0,10,3) #give an horizontal metrix (like a sequence)
print(arange_f)

vector = np.array([1,2,3,4]) #a vector is a one dimensional array
matrix = np.array([[1,2,3,4],[2,5,8,9]]) #a matrix is a two dimensional array
tensor = np.array([[[1,2,3], #A tensor is a generalization of vectors and matrices to n dimensions.
                    [4,5,6],
                    [7,8,9]]])

print(vector,'\n','\n',matrix,'\n','\n',tensor)
print('Dimension:: ',vector.ndim, matrix.ndim, tensor.ndim) #gives dimension
print('Shape', vector.shape, matrix.shape, tensor.shape) #gives rows and column
print('Data type', vector.dtype, matrix.dtype, tensor.dtype) #give data type

original_array = np.arange(1,11)
print(original_array)

reshape_array = original_array.reshape((2,5))
print(f'\n{reshape_array}')

#returns a copy of original array
flatten_array = reshape_array.flatten()
print(f'\n{flatten_array}')

#returns a view of original array not copy
ravel_array = reshape_array.ravel()
print(f'\n{ravel_array}')

trasnpose_array = reshape_array.T
print(f'\n{trasnpose_array}')


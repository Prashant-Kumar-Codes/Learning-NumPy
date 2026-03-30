import numpy as np

'''
Numpy Array as a matrix:
        1-D, 2-D, 3-D, Multidimentional
'''

oneD1 = np.arange(1,11,1)    #same as range
print('oneD1:\n', oneD1)

oneD2 = np.array([i for i in range(1)])
print('oneD2:\n', oneD2)

twoD1 = np.array([[1,2,3],[4,5,6]])

#zero matrix
zero_matrix = np.zeros(shape=(2,4), dtype='int64')
print(zero_matrix)

#one matrix
one_matrix = np.ones((3,3,0), dtype='int32')
print(one_matrix)
print(one_matrix.size)

'''

How to understand the multidimenstional arrays:
    1. 3D of shape - (a, b, c)
        [ outer bracket same for all dimensional arrays ]
        in the outer bracket there will be a number of []
        in each those a brackets there will be b number of []
        in each those b brackets there will be c number of elements/values.
        
        --> number of elements = a*b*c
'''
'''
important methods:
    1> for creating zero matrix: np.zeros(size, dtype=)
    2> for creating ones matrix: np.ones(size, dtype=)
    3> for creating matrix having same value: np.full(size, value)
    4> for creating random matrix: np.random.random(size)

important attributes of array:
    1> array.shape
    2> array.size
    3> array.dtype
    4> array.ndim
    5> array.nbypes
    6> array.T
    7> array.mT
'''
print('Matrix nbytes attribute: ', oneD1.nbytes)
print('Matrix nbytes attribute: ', oneD2.nbytes)
print('Shape of oneD1: ',oneD1.shape)
oneD3 = oneD1.transpose()
print(oneD3.shape)
result = oneD1*oneD3
print(result)
print('Matrix T attribute:\n', twoD1.T)
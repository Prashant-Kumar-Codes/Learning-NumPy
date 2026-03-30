import numpy as np
import time
arr_1d = np.array([1,2,3,4,5,6,7,8,9,10])
arr_2d = np.array([[1,2,3,4],
                   [5,6,7,8],
                   [9,10,11,12]])

'''
[
    [1 2 3], <-- 0th row
    [4 5 6], <-- 1st row  
    [7 8 9] <-- 2nd row
]
similarly for columns
'''
print(arr_1d[1:6]) 
print(arr_2d[1]) #will print whole first row
print(arr_2d[1,2]) #will print a specific element remember the comman(,)
print(arr_2d[:,0]) #all row and 0th column

#sorting array

unsort_array = np.array([1,2,3,4,3,2,1,2,2,6,7,7,5,4,77,88,6,56,4])
print('Sorted Array :: ',np.sort(unsort_array))

unsort_array_2d = np.array([[1,5,3],
                            [9,0,3],
                            [7,3,12]])
print('Sorted 2d Array :: \n',np.sort(unsort_array_2d,axis = 0)) #0 axis means along column side
print('Sorted 2d Array :: \n',np.sort(unsort_array_2d,axis = 1)) #1 axis means along row side

#Filter
number_array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,1,2,1,2,3,4,5,6,7,8,9,10])
t = time.time()
even_array = number_array[number_array%2==0]      #this is also called mask  number_array%2==0  the expressin we write
print('Even_Array :: \n', even_array)
print(time.time()-t)

number_array_2d = np.array([[1,2,3,4,5,6,7,8,9,10,11],
                            [23,44,32,12,3,322,55,65,77,45,34],
                            [0,2847,234,12,534,675,897,678,53,5,9]])
# even_array_2d = number_array_2d[[number_array_2d[0] % 2 == 0],
#                                 [number_array_2d[1] % 2 == 0],
#                                 [number_array_2d[2] % 2 == 0]]
even_array_2d = number_array_2d[number_array_2d % 2 == 0]
print('Even Array 2d :: \n',even_array_2d)

##Filter with mask
mask = number_array > 4
greater_4 = np.array(mask)
print('\n\t\t\t\tgreater_4',greater_4)
greater_4 = number_array[mask]
print('\n',mask)
print('\n\t\t\t\tgreater_4',greater_4)

##Filter with Fancy Indexing
indices = [0,2,3,22,8]
x = number_array[indices]
print(x)

##Filter with where clause
where_result = np.where(number_array % 2 == 0)
where_array = number_array[where_result]
print('Where Result :: \n',where_result,'\n')
print('Where Array :: \n',where_array,'\n')

arrange_array_1 = np.arange(1,5)
arrange_array_2 = np.arange(2,6)
arrange_array_3 = np.arange(3,7)
print(arrange_array_1)

ara = np.array([arrange_array_1,arrange_array_2,arrange_array_3])
print('ara: \n',ara,'\n',ara.ndim)

araa = np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])
print("This is araa: \n", araa,"\n")
x = araa.reshape(2,8)
y = araa.reshape(1,16)
print(x)
print(y)

z = araa.flatten()  #return copy of the array as a row array
zz = araa.ravel()   #return a view of the array as a row array no the copy

print(z,'\n',zz)

transpose = araa.T
print("\n", "This is transpose: \n", transpose)
print("Dimension of transpose: :: ", transpose.ndim)
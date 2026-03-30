import numpy as np

##Array Slicing

a1 = np.arange(1,10)
print("a1:: ", a1)

a1_1 = a1[0:4]
print("a1_1:: ", a1_1)

a2 = np.array([[1,2,3,4],[5,6,7,8]])
print("a2: ", a2, '\n')

a2_1 = a2[1:3] #8
a2_2 = a2[0:,] #1,2,3,4
a2_3 = a2[0:2] #3
a2_4 = a2[0:] #

print("a2_1:: \n", a2_1, '\n')
print("a2_2:: \n", a2_2, '\n')
print("a2_3:: \n", a2_3, '\n')
print("a2_4:: \n", a2_4, '\n')

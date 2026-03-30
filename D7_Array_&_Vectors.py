from numpy import *

#working with vectors using arrays

vec1 = array([1,2,3,45,5])
vec2 = array([4,5,6,7,8])

vec_sum_ =  vec1+vec2
vec_sum = add(vec1,vec2)
vec_suu = sum(vec1) #add the elements of a vector either row or column wise

print(vec_suu)

#array_equal(vector1,vector2) give a single True/False value
print('vec_sum = \n', vec_sum_, '\n', vec_sum, '\n Are the two vectors equal : ', vec_sum_ == vec_sum, '\t', equal(vec_sum_, vec_sum),'\t', array_equal(vec_sum_, vec_sum))


vec_multiplication = vec1 * vec2
print('Vector cross multiplication: ', vec_multiplication)

vec_dot_product = dot(vec1,vec2)
print('Vector cot product: ', vec_dot_product)

#finding angle between the two vectors
# a.b = ab cos0
# 0 = cos-1(a.b / ab)

#np.arccos = cos-1(value) and returns the angle in radian 
angle = arccos(dot(vec1,vec2)/ (linalg.norm(vec1)*linalg.norm(vec2)))
print('Angle between the vec1 and vec2 is : ', degrees(angle))


#vectorised operations:
restaurant_type = array(['Biryai', 'Chinese', 'Pizza', 'burger', 'cafe'])
#vectorize(function) method used to apply normal datatype functions or regular functions to array; element-wise and returns an array
vectorized_upper = vectorize(str.upper)
print('Vectorized Upper : ', vectorized_upper(restaurant_type))


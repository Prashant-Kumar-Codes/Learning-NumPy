import numpy as np

# # Question 1:: Write a Numpy program to get the Numpy version and show the Numpy build configuration.
# #To get version
# print(f"NumPy Version :: {np.__version__}")

# #To get Build Configuration
# print(f"NumPy Build Configuration::")
# np.show_config()

# # Question 2:: Write a NumPy program to get help with the add function.
# print(f'Info for add function:: \n{np.info(np.add)}')

# Write a NumPy program to test whether none of the elements of a given array are zero. 
arr = np.array([[1,2,3,4,1,9,8],[1,2,3,4,5,9,8],[1,2,3,4,9,9,8]])
print(np.all(arr,keepdims = 2))
from numpy import *
import matplotlib.pyplot as plt
from PIL import Image

#saving array as a file
# extension for saving file : npy

arr1 = array([1,2,3,4,6,4])
arr2 = random.rand(3,3)
arr3 = zeros((5,5))

# save('arr1.npy', arr1)
# save('arr2.npy', arr2)
# save('arr3.npy', arr3)

load_arr1 = load('D:\\Codes\\Python\\NumPy\\arr1.npy')
print(load_arr1)

open_img = Image.open("E:\\Pictures\\Images\\numpy_logo.png")
print(type(open_img))
print(open_img)
print(open_img.format)
print(open_img.size)
print(open_img.mode)

numpy_logo_arr = array(open_img)
print(type(numpy_logo_arr))
print(numpy_logo_arr)
numpy_logo_arr = delete(arr=numpy_logo_arr, obj=2, axis=1)
print(numpy_logo_arr.shape)
save('numpy_logo.npy',numpy_logo_arr)

try:
    load_numpy_logo = load('numpy_logo.npy')
    plt.figure(figsize = (10,5))
    plt.subplot(121)
    plt.imshow(load_numpy_logo)
    plt.title('Numpy Logo')
    plt.grid(0)

except FileNotFoundError:
    print('File Not Found')


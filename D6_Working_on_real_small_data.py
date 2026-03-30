import numpy as np
import matplotlib.pyplot as plt
import math
#data sturctue: [restaurant_id, 2021, 2022, 2023, 2024] sales revanue
sales_data = np.array([
        [1, 150000, 180000, 220000, 250000], # Paradise Biryani
        [2, 120000, 140000, 160000, 190000], # Beijing Bites
        [3, 200000, 230000, 260000, 300000], # Pizza Hub
        [4, 180000, 210000, 240000, 270000], # Burger Point
        [5, 160000, 185000, 205000, 230000], # Chai Point
])
######  AXIS 0 (default) = COLUMN WISE,  AXIS 1 = ROW WISE

#checking shape of the array
arr_shape = sales_data.shape
print("Shape of sales_data array:  ", arr_shape)

#print data of first three restaurant
first_3_res_data = sales_data[0:3] # or first_3_res_data = sales_data[:3]
print('data of first three restaurant: \n', first_3_res_data)

###### Working of slicing:: 
# arr[row_slicing, column_slicing]
# e.g. arr[:10, 1:3]

#print the data without restaurant numbering
without_sr_no = sales_data[: , 1:]
print('Data without restaurant serial numbering :\n', without_sr_no)

#print total sales per year
total_sale_per_year = np.sum(sales_data[:, 1:], axis = 0)
print('Total sales per year: \n', total_sale_per_year)

#print minimun sales per restaurant 
min_sales_per_year = np.min(sales_data[:, 1:], axis=1)
min_sales_per_year_col = min_sales_per_year.reshape(-1,1)
#"Is dimension ka size automatically calculate kar lo, bas total elements match karne chahiye."
print('Minimun sales by restaruant per year: \n', min_sales_per_year,'\n',min_sales_per_year_col)

# #TRANSPOSE DOES NOT WORK FOR 1-D ARRAY
# arr = np.array([1,2,4,5])
# print(arr.T)

#print average sales per restaurant
avg_sales = np.average(sales_data[:,1:], axis = 1)
mean_sales = np.mean(sales_data[:, 1:], axis = 1)
print('average sales per restaurant: \n', avg_sales,'\n', mean_sales)

#print cumulative sales
'''
If your sequence is {2, 5, 8, 3}, the cumulative sum / sales sequence would be:
2
2 + 5 = 7
2 + 5 + 8 = 15
2 + 5 + 8 + 3 = 18
The resulting cumulative sum sequence is {2, 7, 15, 18}.
'''

cum_sales = np.cumsum(sales_data[:, 1:], axis = 1)
print('The cumulative sales per year are:\n', cum_sales)

'''
plt.figure(figsize = (10,6))
plt.plot(np.average(cum_sales, axis = 0))
plt.xlabel("Year")
plt.ylabel('Mean Cumulative Sales')
plt.title('The Mean Cumulative Sales Graph of four years')
plt.grid(1)
plt.show()
'''

#brodcast : when a single function to apply to whole array element-wise.
#printing the monthly average of sales_data

montly_average_sales = sales_data[:, 1:] /12
print('Montly average sales for the given years: ', montly_average_sales)

#options for tuncating 
x = 1.28473972
print('Truncate x : ',math.trunc(x))
#for turncating elements in the array
print('Trucated the monthly_average_sales: ',np.trunc(montly_average_sales)) 


#options for rounding
print('Ronnded x :', round(x,3))
print('Rounded array: ', np.round(montly_average_sales,3))
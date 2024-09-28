import numpy as np

# Input list
my_list = [1, 2, 3, 4, 5]

# Convert list to numpy array
numpy_array = np.array(my_list)

# Display the numpy array
print("The NumPy array is:", numpy_array)

# Display the first and last index
first_element = numpy_array[0]
last_element = numpy_array[-1]
print("First element:", first_element)
print("Last element:", last_element)

# Multiply each element by 2
multiplied_array = numpy_array * 2

# Display the result
print("Array after multiplying each element by 2:", multiplied_array)


#OUTPUT:
The NumPy array is: [1 2 3 4 5]
First element: 1
Last element: 5
Array after multiplying each element by 2: [ 2  4  6  8 10]

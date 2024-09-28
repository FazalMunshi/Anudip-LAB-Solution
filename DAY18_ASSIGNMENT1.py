import numpy as np

# Input array of daily temperatures
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2, -4, -12])

# Find days where temperature exceeded 35 degrees (hot days) or dropped below 5 degrees (cold days)
extreme_days = (temperatures > 35) | (temperatures < 5)

# Display the result
print("Extreme temperature days (True for extreme, False for normal):")
print(extreme_days)

# List the temperatures of those extreme days
extreme_temperatures = temperatures[extreme_days]
print("Extreme temperatures:", extreme_temperatures)

#OUTPUT:
Comprehensive Employee Dataset:
[['101' 'John Doe' 'Full-Time' '55000']
 ['102' 'Jane Smith' 'Full-Time' '60000']
 ['103' 'Mike Johnson' 'Full-Time' '52000']
 ['201' 'Alice Brown' 'Part-Time' '25000']
 ['202' 'Bob Wilson' 'Part-Time' '28000']
 ['203' 'Emily Davis' 'Part-Time' '22000']]


def find_largest_and_smallest(numbers):
    # Assume the first number is both the largest and smallest
    largest = numbers[0]
    smallest = numbers[0]
    
    # Iterate through the list starting from the second element
    for number in numbers[1:]:
        if number > largest:
            largest = number  # Update largest if a bigger number is found
        if number < smallest:
            smallest = number  # Update smallest if a smaller number is found
    
    return largest, smallest


my_list = [34, 15, 88, 2, 60, 5, -10]
largest, smallest = find_largest_and_smallest(my_list)
print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")

#OUTPUT:
'''Largest number: 88
Smallest number: -10'''


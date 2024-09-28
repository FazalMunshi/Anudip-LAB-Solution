
def find_duplicates(items):
    seen = []  # To store seen items
    duplicates = []  # To store duplicates
    for item in items:
        if item in seen and item not in duplicates:
            duplicates.append(item)  # Add to duplicates if seen before
        else:
            seen.append(item)  # Otherwise, add to seen list
    return duplicates
my_list = [1, 2, 3, 4, 2, 5, 6, 3, 7, 8, 3]
duplicates = find_duplicates(my_list)
print(f"Duplicate values in the list: {duplicates}")

#OUTPUT:
'''Duplicate values in the list: [2, 3]'''

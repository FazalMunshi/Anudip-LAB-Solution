# Sample dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Create a new dictionary by concatenating the above dictionaries
concatenated_dict = {}

# Update the new dictionary with each dictionary's items
for d in (dic1, dic2, dic3):
    concatenated_dict.update(d)

# Display the concatenated dictionary
print(f"Concatenated Dictionary: {concatenated_dict}")

#output:
'''Concatenated Dictionary: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}'''

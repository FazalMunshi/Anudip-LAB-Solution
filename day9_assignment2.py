def remove_duplicates(input_str):
    result = ""
    seen = set()  # Set to track characters that have already been added to the result
    
    # Loop through each character in the string
    for char in input_str:
        if char not in seen:  # If the character is not in the set, add it to the result
            result += char
            seen.add(char)  # Mark the character as seen
    
    return result

# Test the function with the input string
input_str = "String and String Function"
output_str = remove_duplicates(input_str)
print("Output:", output_str)

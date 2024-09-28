def count_chars_digits_symbols(input_str):
    # Initialize counters
    char_count = 0
    digit_count = 0
    symbol_count = 0

    # Loop through each character in the string
    for char in input_str:
        if char.isalpha():  # Check if the character is a letter
            char_count += 1
        elif char.isdigit():  # Check if the character is a digit
            digit_count += 1
        else:  # Otherwise, it's a symbol
            symbol_count += 1

    # Display the results
    print(f"Chars = {char_count}")
    print(f"Digits = {digit_count}")
    print(f"Symbols = {symbol_count}")

# Test the function with the input string
input_str = "P@#yn26at^&i5ve"
count_chars_digits_symbols(input_str)


#output:
'''Chars = 8
Digits = 3
Symbols = 4
'''

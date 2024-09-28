def get_integer():
    try:
        user_input = input("Please enter an integer: ")
        user_input = int(user_input)
        return f"You entered the integer: {user_input}"
    except ValueError:
        return "Error: That is not a valid integer."

# Test the function
print(get_integer())


#output:
'''Please enter an integer: abc
Error: That is not a valid integer.
Please enter an integer: 42
You entered the integer: 42

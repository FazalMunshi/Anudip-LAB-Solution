# Given string with newline characters
string = "\nBest \nDeeptech \nPython \nTraining\n"

# Remove newline characters
cleaned_string = string.replace("\n", " ")

# Optionally, strip any leading or trailing whitespace
cleaned_string = cleaned_string.strip()

print(cleaned_string)


#output:
#Best Deeptech Python Training

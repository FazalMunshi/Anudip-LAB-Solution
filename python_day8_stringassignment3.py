# Given string
string = "Deeptech Python Training"

# Split the string into words
words = string.split()

# Reverse each word in the list
reversed_words = [word[::-1] for word in words]

# Join the reversed words back into a string
reversed_string = " ".join(reversed_words)

print(reversed_string)

#output:
#hcetpeeD nohtyP gniniarT

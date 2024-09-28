from collections import Counter

# Given sentence
string = "To change the overall look of your document. To change the look available in the gallery"

# Convert the string to lowercase and split it into words
words = string.lower().split()

# Use Counter to count the occurrences of each word
word_counts = Counter(words)

# Print the word counts
for word, count in word_counts.items():
    print(f"'{word}': {count}")

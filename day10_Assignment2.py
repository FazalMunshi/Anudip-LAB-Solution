def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()  # Read the entire content of the file
            words = content.split()  # Split the content into words
            word_count = len(words)  # Count the number of words
            print(f"Total number of words: {word_count}")
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")


#output:
'''Hello, World!
This is a test file with seven words.
'''
        

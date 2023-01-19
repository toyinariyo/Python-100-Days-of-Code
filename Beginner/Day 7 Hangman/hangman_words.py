print("Loading wordlist from file...")
file_open = open("wordlist_file.txt", 'r')
word_list = [line for line in file_open]  # Used list comprehension instead of for loop to make code more Pythonista.
print(" ", len(word_list), " words found.")

print("Loading wordlist from file...")
file_open = open("wordlist_file.txt", 'r')
word_list = []
for line in file_open:
    word_list.append(line.strip().lower())
print(" ", len(word_list), " words found.")

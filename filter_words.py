# Filter words that are not 5 letters
with open("words.txt", "r") as f, open("words_filtered.txt", "w") as f2:
    for line in f:
        if len(line.strip()) == 5:
            f2.write(line)

with open("ai_cognizance/about.txt", "r") as fh:
    text = fh.read()

words = text.split()  # Split the text into words

word_count = {}
for word in words:
    if len(word) >= 6:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

# Find the word with the highest count
max_word = max(word_count, key=word_count.get)
max_count = word_count[max_word]

print("Word counts:")
print(word_count)
print(f"The word with the highest count is '{max_word}' with a count of {max_count}.")

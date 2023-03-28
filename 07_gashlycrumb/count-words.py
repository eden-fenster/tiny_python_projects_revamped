text = "To be or not to be, that is the question"
clean_text = text.replace(",", "")
words = clean_text.split()
counts = {}
for word in words:
    clean_word = word.lower()
    if clean_word in counts:
        counts[clean_word] += 1
        continue
    counts[clean_word] = 1
# for (word, count) in counts.items():
#     print(word, count)

word_list = list(counts.keys())
word_list.sort()
for word in word_list:
    print(word, counts[word])
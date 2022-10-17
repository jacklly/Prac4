"""
Word Occurrences
Time Estimate:

"""

words_dictionary = {}
text = input("Please input your text: ").lower()

words = text.split()
"""this means a sorting program is not required, making the code more efficient"""
words.sort()
longest_word = max((len(word) for word in words))

for word in words:
    if word not in words_dictionary:
        words_dictionary[word] = 0
    words_dictionary[word] += 1


for set in words_dictionary:
    print(f"{set:{longest_word}}: {words_dictionary[set]}")
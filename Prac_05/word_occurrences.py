"""
Word Occurrences
Time Estimate:

"""

words_dictionary = {}
text = input("Please input your text: ").lower()

words = text.split()
words.sort()

for word in words:
    if word not in words_dictionary:
        words_dictionary[word] = 0
    words_dictionary[word] += 1

for set in words_dictionary:
    print(f"{set} occurs {words_dictionary[set]} times")

print(words_dictionary)

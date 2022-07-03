def longest_word(words_list):
    word_length = []
    for word in words_list:
        word_length.append((len(word), word))
    word_length.sort()
    return word_length[-1][0], word_length[-1][1]
result = longest_word(["cat", "horse", "elephant","dog"])
print("\nThe Longest word: ",result[1])
print("Length of the longest word: ",result[0])
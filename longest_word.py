def get_longest_word(ls_sentence):
    longest_word = ls_sentence[0]
    for word in ls_sentence:
        if len(longest_word) < len(word):
            longest_word = word

    return longest_word

sentence = "Thehjdhdhhdhss longest word should be loooongg"
ls_sentence = sentence.split()
print(get_longest_word(ls_sentence))

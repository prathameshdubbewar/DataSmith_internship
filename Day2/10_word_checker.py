def word_in_sentence(sentence, word):
    if word.lower() in sentence.lower():
        return True


input_sentence = input("Enter a sentence: ")
input_word = input("Enter a word to check: ")

result = word_in_sentence(input_sentence, input_word)

if result == True:
    print(f"The word {input_word} is present in the sentence.")
else:
    print(f"The word {input_word} is not present in the sentence.")

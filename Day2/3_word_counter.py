def count_word(sent):
    word = sent.split()
    return len(word)

sentence = input("enter your sentence: ")
count = count_word(sentence)
print("number of words in sentences are : ",count)
def concatenate_words(word):
    concatenated_string = ' '.join(word)
    return concatenated_string

list = input("enter words seperated by spaces: ")
words = list.split()
result = concatenate_words(words)

print("String output : ", result)

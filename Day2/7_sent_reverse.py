def reverse_sentence(input_sentence):
    words = input_sentence.split()
    reversed_sentence = ' '.join(words[::-1])
    return reversed_sentence


input_sentence = input("Enter a sentence: ")
result = reverse_sentence(input_sentence)

print("Reversed Sentence:", result)

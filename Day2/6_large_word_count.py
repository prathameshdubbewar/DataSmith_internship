def word_count(sent):
    words = sent.split()
    max_len = max(len(i) for i in words)
    return max_len

sent = input("enter the sentence: ")
max_count = word_count(sent)
print(max_count)
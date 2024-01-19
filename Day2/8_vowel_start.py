def vowel_start (names_list):
    vowels = "aeiouAEIOU"
    sorted_words = []

    for i in names_list:
        if i[0] in vowels:
            sorted_words.append(i)

    return sorted_words



names_input = input("Enter a list of names separated by spaces: ")
names_list = names_input.split()

words_list = vowel_start(names_list)
print("count of words starting with vowels is: ",len(words_list))
print("words starting with vowels are : ",words_list)


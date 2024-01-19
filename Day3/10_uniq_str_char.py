def unique_characters(strings):
    unique_chars = set().union(*map(set, strings))
    return unique_chars

string_list = input("Enter a list of strings : ").split()


result = unique_characters(string_list)
print("Unique characters:", result)

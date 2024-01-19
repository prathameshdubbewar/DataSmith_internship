def remove_duplicates(input_string):
    unique_characters = set()
    result_string = ''

    for i in input_string:
        if i not in unique_characters:
            unique_characters.add(i)
            result_string += i

    return result_string

input_str = input("Enter a string: ")
result = remove_duplicates(input_str)

print("resultant string is: ", result)

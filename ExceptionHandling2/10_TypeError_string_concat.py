def concat_strings(string_list):
    try:
        concatenated_string = ''.join(string_list)
        return concatenated_string
    except TypeError:
        print("Error: Non-string element encountered in the list.")
        return None

input_list = ['hello', 'world', '!']  
result = concat_strings(input_list)
if result is not None:
    print("Concatenated string:", result)

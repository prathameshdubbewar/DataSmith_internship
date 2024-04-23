def concat_strings(string_list):
    try:
        concatenated_string = ''.join(string_list)
        return concatenated_string
    except TypeError:
        print("Error: Non-string element encountered in the list.")
        return None

# input_list = ['hello', 'world', '!']  
input_list = input("enter all the inputs: ")
new_list = input_list.split()
print(input_list)

result = concat_strings(new_list)
if result is not None:
    print("Concatenated string:", result)

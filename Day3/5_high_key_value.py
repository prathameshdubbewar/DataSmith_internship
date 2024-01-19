def max_dict(list_of_dicts, value_to_check):
    if not list_of_dicts:
        print("List of dictionaries is empty.")
        return None

    max_dict = max(list_of_dicts, key=lambda x: x.get(value_to_check, 0))
    return max_dict


num_of_dict = int(input("Enter number of dicts"))
list_of_dicts = []
for i in range(num_of_dict):
    input_dict = input(f"Enter dictionary {i + 1} in the format key1:value1,key2:value2: ")
    dict_elements = dict(item.split(':') for item in input_dict.split(','))
    list_of_dicts.append(dict_elements)

value_to_check = input("enter the value to check")

max_dictionary = max_dict(list_of_dicts, value_to_check)

if max_dictionary:
    print(f"The dictionary with the highest value for key '{value_to_check}' is:")
    print(max_dictionary)


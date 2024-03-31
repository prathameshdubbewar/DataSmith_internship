def get_value_from_dict(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        print(f"The key '{key}' is not present in the dictionary.")
        return None


my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_find = 'b'
value = get_value_from_dict(my_dict, key_to_find)
print(f"The value with key '{key_to_find}' is: {value}")
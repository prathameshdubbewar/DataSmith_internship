def dict_check(dictionary, key_to_check):
    try:
        if not isinstance(dictionary, dict):
            raise TypeError("Input must be a dictionary")

        return dictionary.get(key_to_check)

    except TypeError as e:
        print(f"TypeError: {e}")
        return None

# use to take dict from user
my_dict = {}
while True:
    key = input("Enter key or type 'done' to finish: ")
    if key.lower() == 'done':
        break
    value = input(f"Enter value for key '{key}': ")
    my_dict[key] = value
print(my_dict)
# to check exception
new_lst =[2,'d',4]
# my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_check = 'b'
print(f"The value associated with key '{key_to_check}' is: {dict_check(new_lst, key_to_check)}")


def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

input1 = input("Enter 1st dict in the format key1:value1,key2:value2: ")
dict1 = dict(item.split(':') for item in input1.split(','))
print(dict1)

input2 = input("Enter 2nd dict in the format key3:value3,key4:value4: ")
dict2 = dict(item.split(':') for item in input2.split(','))
print(dict2)


result_dict = merge_dicts(dict1, dict2)

print("Merged Dict:", result_dict)

def sort_dicts(list_of_dicts, key_to_sort):
        for i in range(len(list_of_dicts)):
            for j in range(i + 1, len(list_of_dicts)):
                if list_of_dicts[i].get(key_to_sort, 0) > list_of_dicts[j].get(key_to_sort):
                    list_of_dicts[i], list_of_dicts[j] = list_of_dicts[j], list_of_dicts[i]

        # other way
        # sorted_list = sorted(list_of_dicts, key=lambda x: x.get(key_to_sort, 0))
                    
        return list_of_dicts

list_of_dictionaries = [
    {'name': 'pratham', 'age': 25, 'score': 90},
    {'name': 'ved', 'age': 30, 'score': 85},
    {'name': 'sonu', 'age': 28, 'score': 95}
]

key_to_sort = 'score'

sorted_list_of_dicts = sort_dicts(list_of_dictionaries, key_to_sort)

print(f"Sorted list of dictionaries based on '{key_to_sort}':")
print(sorted_list_of_dicts)


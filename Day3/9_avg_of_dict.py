def average_value(list_of_dicts, key_to_average):

    total_value = sum(d.get(key_to_average, 0) for d in list_of_dicts)
    average = total_value / len(list_of_dicts)
    return average


list_of_dictionaries = [
    {'name': 'pratham', 'age': 25, 'score': 90},
    {'name': 'ved', 'age': 30, 'score': 85},
    {'name': 'sonu', 'age': 28, 'score': 95}
]

key_age = 'age'
key_score = 'score'

average_age = average_value(list_of_dictionaries, key_age)
average_score = average_value(list_of_dictionaries, key_score)

print(f"Average age: {average_age}")
print(f"Average score: {average_score}")

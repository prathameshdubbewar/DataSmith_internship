def calculate_average(list_of_dicts):
    if not list_of_dicts:
        print("List is empty.")
        return None

    total_sum = 0
    total_elements = 0

    for dictionary in list_of_dicts:
        for value in dictionary.values():
            if isinstance(value, (int, float)):
                total_sum += value
                total_elements += 1

    if total_elements == 0:
        print("No integerfound.")
        return None

    average = total_sum / total_elements
    return average

list_of_dictionaries = [
    {'name': 'pratham', 'age': 25, 'score': 90},
    {'name': 'ved', 'age': 30, 'score': 85},
    {'name': 'sonu', 'age': 28, 'score': 95}
]

average_value = calculate_average(list_of_dictionaries)
print(f"The average valueis: {average_value}")

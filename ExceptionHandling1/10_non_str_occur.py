def string_lengths(input_list):
    lengths = []
    for item in input_list:
        try:
            lengths.append(len(item))
        except TypeError:
            print(f"Error: Non-string element '{item}' encountered.")
            return None
    return lengths


example_input = ['apple', 'banana', 123, 'orange', 'grape']

result = string_lengths(example_input)

print("Result:", result)

def str_to_int(input_str):
    try:
        int_value = int(input_str)
        return int_value
    
    except ValueError:
        print("Error: cannot convert string to int.")
        return None

input_string = input("Enter a input to convert: ")
result = str_to_int(input_string)
if result is not None:
    print("Integer value:", result)

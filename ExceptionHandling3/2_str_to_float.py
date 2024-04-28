def string_to_float(input_str):
    try:
        float_num = float(input_str)
        return float_num
    except ValueError:
        print("Error: cannot convert str to float")
        return None

input_str = input("Enter a string to convert: ")
result = string_to_float(input_str)
if result is not None:
    print("Float value:", result)

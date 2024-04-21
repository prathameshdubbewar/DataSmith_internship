def sqr_of_int(input_str):
    try:
        int_value = int(input_str)
        return int_value**2
    
    except ValueError:
        print("Error: cannot convert string to int.")
        return None
        

user_input = input("Enter a input to convert: ")
result = sqr_of_int(user_input)
if result is not None:
    print("Integer value:", result)


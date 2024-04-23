def prodct_of_ints(int_list):
    try:
        product = 1
        for num in int_list:
            product *= num
        return product
    
    except TypeError:
        print("Error: The value is not int.")
        return None

input_list = input("Enter a list of integers: ")
integers = [int(num) for num in input_list.split()]
result = prodct_of_ints(integers)
if result is not None:
    print("Product:", result)

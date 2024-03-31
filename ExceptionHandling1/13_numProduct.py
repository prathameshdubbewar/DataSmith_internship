def calculate_product(numbers):
    
    product = 1
    for num in numbers:
        try:
            product *= float(num)
        
        except ValueError:
            print("Error: input is not integer.")
    return product


user_input = input("Enter a sequence of numbers: ")
number_list = user_input.split()


result = calculate_product(number_list)
print("Product:", result)

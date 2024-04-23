def sum_of_ints(int_list):
    try:
        sum = 0
        for num in int_list:
            sum *= num
        return sum
    
    except ValueError:
        print("Error: The value is not int.")
        return None

input_list = input("Enter a list of integers: ")
integers = [int(num) for num in input_list.split()]
result = sum_of_ints(integers)
if result is not None:
    print("Sum is :", result)

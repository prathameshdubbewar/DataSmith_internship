def calc_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

try:
    input_string = input("Enter a list of integers: ")

    numbers = [int(num) for num in input_string.split('')]

    product = calc_product(numbers)

    print("Product of  numbers is :", product)

except ValueError:
    print("Error: Input is not int")

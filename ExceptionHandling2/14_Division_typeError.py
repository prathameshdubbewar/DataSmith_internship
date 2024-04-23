def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

try:
    num1 = float(num1)
    num2 = float(num2)
except ValueError:
    print("Error: input is not a number.")
else:
    result = divide_numbers(num1, num2)
    if result is not None:
        print("Result is: ", result)


def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = divide_numbers(num1, num2)
if result is not None:
    print(f"The result of division of {num1} by {num2} is: {result}")

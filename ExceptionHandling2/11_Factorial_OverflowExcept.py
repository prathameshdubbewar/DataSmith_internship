import math

try:
    num = int(input("Enter an integer: "))
    
    factorial = math.factorial(num)
    
    print(f"The factorial of {num} is: {factorial}")
    
except ValueError:
    print("Error: enter a valid integer.")
except OverflowError:
    print("Error: exceeds the maximum integer value.")


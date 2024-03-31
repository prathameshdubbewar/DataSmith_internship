
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
        
    result = num1 / num2
        
    print("Result:", result)
    
except ZeroDivisionError:
        print("Error: Enter a non-zero second number.")

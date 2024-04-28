
try:
    number = input("Enter a number: ")
    
    number = float(number)
    
    square_root = number **0.5
    
    print(f"The square root of {number} is: {square_root}")


except TypeError:
    print("Error: Input must be a numeric.")

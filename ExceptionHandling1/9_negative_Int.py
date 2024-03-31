try:
    number = int(input("Enter a number: "))
    if number < 0:
        raise ValueError("Input is negative")
    square_root = number ** 0.5
    print(f"The square root of {number} is: {square_root}")
except ValueError as ve:
    print("Error:", ve)

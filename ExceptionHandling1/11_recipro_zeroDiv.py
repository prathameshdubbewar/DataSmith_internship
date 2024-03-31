try:
    number = float(input("Enter a number: "))
    reciprocal = 1 / number
    print(f"The reciprocal of {number} is: {reciprocal}")
except ZeroDivisionError:
    print("Error: number cannot be zero.")

def power(base, exponent):
    result = base ** exponent
    return result

base_input = input("Enter the base number: ")
exponent_input = input("Enter the exponent number: ")

try:
    base = float(base_input)
    exponent = float(exponent_input)
    print("Result:", power(base, exponent))
except ValueError:
    print("Error: Both inputs must be numeric.")


# OR

def power():
    try:
        base_input = input("Enter the base number: ")
        base = float(base_input)
        exponent_input = input("Enter the exponent number: ")
        exponent = float(exponent_input)
        result = base ** exponent
        print("Result:", result)
    except ValueError:
        print("Error: Both inputs must be numeric.")

power()

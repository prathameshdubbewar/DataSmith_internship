try:
    numbers = input("Enter a sequence of numbers : ").split()
    numbers = [float(num) for num in numbers]
    total = sum(numbers)
    print("Sum of the numbers:", total)
except KeyboardInterrupt:
    print("Program interrupted by the user.")

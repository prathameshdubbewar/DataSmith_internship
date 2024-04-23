def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

try:
    file_name = input("Enter file name: ")
    with open(file_name, 'r') as file:
        numbers = [float(line.strip()) for line in file.readlines()]
    average = calculate_average(numbers)
    print("Average of numbers in the file:", average)
except FileNotFoundError:
    print("Error: File not found.")
except ValueError:
    print("Error: Invalid data in the file.")

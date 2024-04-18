try:
    nums = input("Enter a list of numbers separated by commas: ")
    
    num_list = [float(num) for num in nums.split(',')]

    average = sum(num_list) / len(num_list)
    
    print("Average:", average)

except ValueError:
    print("Error: The input is not a number.")

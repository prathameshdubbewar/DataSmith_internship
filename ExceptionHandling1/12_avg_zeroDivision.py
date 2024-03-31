def average_of_list(lst):
    try:
        avg = sum(lst) / len(lst)
        return avg
    except ZeroDivisionError:
        print("Error: The list is empty.")
        

user_input = input("Enter a list of integers: ")
input_list = [int(x) for x in user_input.split()]
print("Average:", average_of_list(input_list))

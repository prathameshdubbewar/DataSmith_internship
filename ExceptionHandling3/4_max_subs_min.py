def max_min_diff(int_list):
    try:
        if not int_list:
            raise IndexError("Input list is empty")
        
        max_num = max(int_list)
        min_num = min(int_list)
        return max_num - min_num
    except IndexError as ie:
        print(f"Error: {ie}")
        return None

user_input = input("enter the numbers: ")
input_lst  = [int(num) for num in user_input.split()]
result = max_min_diff(input_lst)
if result is not None:
    print("Diff between max and min is : ", result)


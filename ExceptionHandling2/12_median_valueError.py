def calculate_median(int_list):
    try:
        if not int_list:
            raise ValueError("Input list is empty")
        
        sorted_list = sorted(int_list)
        
        n = len(sorted_list)
        if n % 2 == 0:
            median = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
        else:
            median = sorted_list[n // 2]
        
        return median
    
    except ValueError as e:
        print(f"Error: {e}")
        return None

input_list = [5, 2, 8, 4, 1, 9, 3]
median = calculate_median(input_list)
if median is not None:
    print("Median:", median)


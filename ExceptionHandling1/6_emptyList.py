def find_max(numbers):
    try:
        if len(numbers) == 0:
            raise ValueError("List is empty")
        
        max_num = max(numbers)
        return max_num
        
    except ValueError as e:
        print("Error:", e)
        
    
nums = []
print(find_max(nums))
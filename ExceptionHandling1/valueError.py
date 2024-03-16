def sum_of_no():
    lst = input("Enter a list of integers: ").split()
    total = 0
    for ele in lst:
        try:
            total += int(ele)
        except ValueError:
            print(f" non-integer element : {ele}")
    return total

print("Sum of elements is :", sum_of_no())

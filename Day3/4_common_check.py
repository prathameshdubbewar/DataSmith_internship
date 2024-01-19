def common_check(set1, set2):
    common_ele = set1.intersection(set2)
    return common_ele


set1_input = input("Enter first set : ")
set2_input = input("Enter second set : ")

set1 = set(map(int, set1_input.split()))
set2 = set(map(int, set2_input.split()))
result = common_check(set1, set2)

print("number of common elements are : ",len(result))
print("common elements are : ",result)

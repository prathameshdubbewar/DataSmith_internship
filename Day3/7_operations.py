def set_operations(set1, set2):
    union_set = set1.union(set2)
    intersection_set = set1.intersection(set2)
    difference_set1_minus_set2 = set1.difference(set2)
    difference_set2_minus_set1 = set2.difference(set1)

    return union_set, intersection_set, difference_set1_minus_set2, difference_set2_minus_set1

set1_input = input("Enter first set : ")
set2_input = input("Enter second set : ")

set1 = set(map(int, set1_input.split()))
set2 = set(map(int, set2_input.split()))

union_result, intersection_result, difference_result1, difference_result2 = set_operations(set1, set2)

print("Union of sets:", union_result)
print("Intersection of sets:", intersection_result)
print("Difference (Set1 - Set2):", difference_result1)
print("Difference (Set2 - Set1):", difference_result2)

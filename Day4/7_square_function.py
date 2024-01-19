import numpy as np

def squared_nums(arr_lst):
    arr_squared = ([int(i)**2 for i in given_lst])

    squared_lst = np.square(arr_lst)
    return squared_lst , arr_squared

given_lst = input("enter the elements for array: ").split()

arr_lst = np.array([int(i) for i in given_lst])
print(arr_lst)
sqr1,sqr2 = squared_nums(arr_lst)
print("squared values of the elements are:")
print("using np: ",sqr1)
print("using operations",sqr2) 
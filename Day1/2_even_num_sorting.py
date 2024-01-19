
def sort(numbers):
    evens = []
    for i in numbers:
        if i % 2 == 0:
            evens.append(i)
    return evens

lst = []

numbers_input = input("Enter numbers separated by spaces: ")

# list1 = [int(num) for num in numbers_input.split()]

for i in numbers_input.split():
    if i.isdigit():
        lst.append(int(i))

output = sort(lst)

print(output)



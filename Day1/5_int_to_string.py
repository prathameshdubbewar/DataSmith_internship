
n = int(input("Enter a number: "))


num_list = []
for i in range(1, n + 1):
    num_list.append(str(i))

num_string = ""
for i in num_list:
    num_string += i

print(num_string)



def operations(lst):
    print("The initial list")
    print(lst)

    num = n
    lst.insert(1,num)
    print("insert n at position i")
    print(lst)

    if num in lst:
        lst.remove(num)
    print("removed first occurence of n")
    print(lst)

    lst.append(n)
    print("added n at end of list")
    print(lst)

    lst.sort()
    print("sorted list")
    print(lst)

    lst.pop()
    print("popped last element")
    print(lst)

    lst = lst[::-1]
    print("reversed list")
    print(lst)


lst = []
n = 4

for i in range(1, n+1):
    lst.append(i)

operations(lst)

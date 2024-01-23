def fibonacci_non_recursive(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b     


def fibo_recur(n):
    if n<=1:
        return 1
    
    else :
        fibo_recur(n-1) + fibo_recur(n-2)

n=int(input("enter the value of n for your fib no"))
output = fibonacci_non_recursive(n)
print(f"The fibo value of '{n}' th value is: " ,output)

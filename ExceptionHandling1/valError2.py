def factorial(num):
    result = 1
    for i in range(2,num+1):
        result *= i
    return result

try:
    num = int(input("enter the number: "))
    print(f"the factorial of {num} is {factorial(num)}")

except ValueError:
    print("Invalid input: The num is not integer")

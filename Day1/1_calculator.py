def calculator():
    
    num1 = int(input("Enter your first num: "))
    operator = input("select operation to do (+, -, *, /): ")
    num2 = int(input("Enter your second num: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        
        if num2 != 0:
            result = num1 / num2
        else:
            print("cannot divide by 0")
            return
    else:
        print("Invalid operator input , select correct operator")
        return

    
    print(f"Result: {num1} {operator} {num2} = {result}")


calculator()

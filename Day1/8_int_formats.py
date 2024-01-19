def print_formatted_numbers(n):
    width = len(bin(n)[2:])  

    for i in range(1, n + 1):
        decimal_str = format(i, '>{width}d'.format(width=width))
        octal_str = format(i, '>{width}o'.format(width=width))
        hex_str = format(i, '>{width}X'.format(width=width))
        binary_str = format(i, '>{width}b'.format(width=width))

        print(f"{decimal_str}      {octal_str}     {hex_str}       {binary_str}")


n = int(input("Enter an integer: "))
print("deci_str  oct_str  hex_str  bin_str")

print_formatted_numbers(n)

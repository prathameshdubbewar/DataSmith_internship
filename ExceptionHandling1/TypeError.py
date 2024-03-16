def concat_str(str1,str2):
    try:
        str1 = str(input("enter string 1: "))
        str2 = str(input("enter string 2: "))
        result = str1 + str2
        print("resultant string is:",result)
    except TypeError:
        print("Error: inputs must be string")




result = concat_str()
print("resultant str is:", result)
def vowel_filter(str):
    vowels = "aeiouAEIOU"
    outputstr = "".join(i for i  in str if i not in vowels)
    return outputstr

str = input("enter a string :")
result = vowel_filter(str)
print("String without vowels is: ",result)
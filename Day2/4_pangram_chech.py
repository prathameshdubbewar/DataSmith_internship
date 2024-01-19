def pangram_check(inpt_str):
    alphabets = "abcdefghijklmnopqrstuvwxyz"

    return all(char in inpt_str.lower() for char in alphabets)
    # OR
    # for i in alphabets:
    #     if i not in inpt_str.lower():
    #         return False
        
    # return True

inpt_str = input(" give the sentence: ")
result = pangram_check(inpt_str)  
print("is sentence pangram : ",result)
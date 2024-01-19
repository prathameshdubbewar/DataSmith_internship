def freq_element(lst):
    freq_dict = {}

    for ele in lst:
        if ele in freq_dict:
            freq_dict[ele] +=1

        else :
            freq_dict[ele] = 1

    
    freq_ele = max(freq_dict, key=freq_dict.get)
    return freq_ele , freq_dict[freq_ele]
        

input_lst = input(" enter list of elements:  ")
elements = input_lst.split()

result,freq = freq_element(elements)

print(f"most frequent is '{result}' with freq of '{freq}'")
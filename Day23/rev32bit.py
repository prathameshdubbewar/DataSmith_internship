n =" 00000010100101000001111010011100"
n="".join(n[::-1])
n=int(n)
print(n)

res =0
j=0
while n > 0:
    lst_digit = n% 10
    res += lst_digit*(2**j)
    j +=1
    n=n//10
print(res)

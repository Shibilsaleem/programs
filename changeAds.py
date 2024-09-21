def changeAds(n):
    b=bin(n)[2:]
    b1=''
    decimal=0
    for bit in b:
        if bit=='1':
            b1=b1+'0'
        else:
            b1=b1+'1'
    for i in range(len(b1)):
        decimal+=int(b1[i])*(2**(len(b1)-(i+1)))
    return decimal
print(changeAds(50))
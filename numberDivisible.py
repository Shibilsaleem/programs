def number(n):
    ct=0
    if n%5==0:
        res=n/5
    elif n%3==0:
        res=n/3
    elif n%2==0:
        res=n/2
    else:
        while(n>0):
            n=n-1
            ct+=1
        return ct
    return res
n=int(input('Enter the number : '))
print(number(n))
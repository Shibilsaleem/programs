def phNumber(s):
    number=''
    ct=0
    i=len(s)-1
    while(ct<=10):
        if s[i].isdigit():
            number+=s[i]
            ct+=1
            i-=1
        else:
            i-=1
    number=number[::-1]
    return number
s=input('Enter the input : ')
print(phNumber(s))
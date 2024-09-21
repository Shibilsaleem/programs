def alphabett(s):
    res=''
    for i in range(len(s)):
        if s[i].isalpha():
            char=s[i]
        i+=1
        num=0
        while i<len(s) and s[i].isdigit():
            num=num*10+int(s[i])
            i+=1
        res+=(char*num)
    return res
s=input('Enter the input: ')
print(alphabett(s))

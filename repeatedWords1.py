def repeatedWords(s,n):
    words={}
    res=[]
    l=s.split()
    for ele in l:
        if ele in words:
            words[ele]+=1
        else:
            words[ele]=1
    for key,val in words.items():
        if int(val)>=n:
            res.append(key)
    if not res:
        print('NA')
    else:
        return res
s=input('Enter the input string : ')
n=int(input('Ener the count : '))
print(repeatedWords(s,n))
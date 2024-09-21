def findFactor(s):
    mydict={}
    fac=[]
    facofs=[]
    res=[]
    for ele in s:
        if ele not in mydict:
            mydict[ele]=1
        else:
            mydict[ele]+=1
    for key,val in mydict.items():
        if val==4:
            temp=int(key)
            for i in range(1,temp+1):
                if temp%i==0:
                    fac.append(i)
    length=len(s)
    for i in range(1,length+1):
        if length%i==0:
            facofs.append(i)
    for ele in fac:
        if ele in facofs:
            res.append(ele)
    ans=len(res)
    #print(res)
    print(fac)
    print(facofs)
    return ans
    
s='888800'
print(hi(s))



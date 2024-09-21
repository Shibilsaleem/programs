def removeChar(s,t):
    new=[]
    count=0
    for ele in s:
        temp=s.replace(ele,'')
        new.append(temp)
    for word in new:
        for ele in t:
            if word==ele:
                count+=1
    return count
n=int(input('Enter length of string : '))
s='abcde'
m=int(input('Enter no of strings in t : '))
t=list(map(str,input('Enter strings : ').split()))
print(removeChar(s,t))

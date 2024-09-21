def count_as_prefix(s):
    store={}
    res=''
    for char in s:
        if char not in store:
            store[char]=1
        else:
            store[char]+=1
    for key,val in store.items():
        res+=str(val)
        res+=key
    return res
s=input('Enter the input string : ')
print(count_as_prefix(s))
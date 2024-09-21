def string_to_dict(s):
    mydict={}
    s=s.split('&')
    for ele in s:
        ele=ele.split('=')
    for i in range(0,len(s),2):
        mydict[s[i]]=s[i+1]
    return mydict
s=input(('Enter the string : '))
print(string_to_dict(s))
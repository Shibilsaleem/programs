
def iterate(l1,start,end):
    if start<0 or start>=end:
        return
    print(l1[start])
    iterate(l1,start+1,end)
l1=eval(input('Enter the list : '))
start=int(input('enter start index : '))
end=int(input('enter end index : '))
print(iterate(l1,start,end))

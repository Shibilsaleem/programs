def absDifference(a):
    difference=[]
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            difference.append(abs(a[i]-a[j]))
    M,m=max(difference),min(difference)
    res=5*M-m
    return res
array=list(map(int, input('Enter array : ').split()))
print(absDifference(array))
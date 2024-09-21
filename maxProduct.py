def productPair(arr):
    prod=float('-inf')
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]*arr[j]>prod:
                prod=arr[i]*arr[j]
                n1,n2=arr[i],arr[j]
    return (n1,n2)
a=[5,3,1,4,3,7,6,9,2]
print(productPair(a))
def targetStep(n,target):
    step=0
    res=n*n
    while res<=target:
        step+=1
        if res==target:
            return step
        res=res*n
    return -1
n=int(input('Enter the number : '))
t=int(input('Enter the target : '))
print(targetStep(n,t))
    
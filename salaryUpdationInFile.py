n1=int(input('Enter number : '))
target=int(input('Enter target : '))
ct=0
temp=n1*n1
while True:
    if temp==target:
        ct+=1
        break
    else:
        temp=temp*n1
        ct+=1
print(ct)
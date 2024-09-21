def nonBinary(a):
    binary=[]
    decimal=[]
    for i in range(len(a)):
        temp=bin(a[i])[2:-2]
        decimal.append(int(temp,2))
    su=sum(decimal)
    return su
integers=eval(input('Enter the array of integers : '))
print(nonBinary(integers))